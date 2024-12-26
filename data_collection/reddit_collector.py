import praw

class RedditCollector:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)

    def collect_posts(self, subreddit, limit=100):
        posts = []
        for post in self.reddit.subreddit(subreddit).hot(limit=limit):
            posts.append({
                'title': post.title,
                'text': post.selftext,
                'created_utc': post.created_utc,
                'author': str(post.author),
                'score': post.score,
                'num_comments': post.num_comments
            })
        return posts
