from flask import Flask, render_template, request, jsonify
from data_collection.twitter_collector import TwitterCollector
from data_collection.reddit_collector import RedditCollector
from preprocessing.text_preprocessor import TextPreprocessor
from sentiment_analysis.sentiment_classifier import SentimentClassifier
from visualization.dashboard import Dashboard

app = Flask(__name__)

# Initialize components
twitter_collector = TwitterCollector('API_KEY', 'API_SECRET_KEY', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
reddit_collector = RedditCollector('CLIENT_ID', 'CLIENT_SECRET', 'USER_AGENT')
preprocessor = TextPreprocessor()
classifier = SentimentClassifier()
dashboard = Dashboard()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    query = request.form['query']
    platform = request.form['platform']
    
    # Collect data
    if platform == 'twitter':
        data = twitter_collector.collect_tweets(query)
    else:
        data = reddit_collector.collect_posts(query)
    
    # Preprocess and analyze
    preprocessed_texts = [preprocessor.preprocess(item['text']) for item in data]
    sentiments = classifier.predict(preprocessed_texts)
    
    # Prepare results
    results = []
    for item, sentiment in zip(data, sentiments):
        results.append({
            'text': item['text'],
            'sentiment': sentiment,
            'created_at': item['created_at']
        })
    
    # Create visualizations
    sentiment_counts = {label: list(sentiments).count(label) for label in set(sentiments)}
    pie_chart = dashboard.create_sentiment_pie_chart(sentiment_counts)
    time_series = dashboard.create_sentiment_over_time(pd.DataFrame(results))
    
    return jsonify({
        'results': results,
        'pie_chart': pie_chart.to_json(),
        'time_series': time_series.to_json()
    })

if __name__ == '__main__':
    app.run(debug=True)
