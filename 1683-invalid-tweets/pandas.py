import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets = tweets[tweets['content'].str.len() > 15]
    result = invalid_tweets[['tweet_id']]
    return result
