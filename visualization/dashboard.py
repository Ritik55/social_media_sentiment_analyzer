import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

class Dashboard:
    @staticmethod
    def create_sentiment_pie_chart(sentiment_counts):
        labels = ['Positive', 'Neutral', 'Negative']
        values = [sentiment_counts.get(label, 0) for label in labels]
        
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title_text='Sentiment Distribution')
        return fig

    @staticmethod
    def create_sentiment_over_time(df):
        df['date'] = pd.to_datetime(df['created_at'])
        sentiment_over_time = df.groupby([df['date'].dt.date, 'sentiment']).size().unstack(fill_value=0)
        
        fig = px.line(sentiment_over_time, x=sentiment_over_time.index, y=['Positive', 'Neutral', 'Negative'])
        fig.update_layout(title_text='Sentiment Over Time', xaxis_title='Date', yaxis_title='Count')
        return fig
