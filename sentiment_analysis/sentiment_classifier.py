from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class SentimentClassifier:
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB()),
        ])

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
