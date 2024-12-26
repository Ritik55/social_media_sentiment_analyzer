import tweepy
from datetime import datetime, timedelta

class TwitterCollector:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def collect_tweets(self, query, count=100):
        tweets = []
        for tweet in tweepy.Cursor(self.api.search_tweets, q=query, lang="en").items(count):
            tweets.append({
                'text': tweet.text,
                'created_at': tweet.created_at,
                'user': tweet.user.screen_name,
                'retweet_count': tweet.retweet_count,
                'favorite_count': tweet.favorite_count
            })
        return tweets
