# tiktok_data_collector.py
from TikTokApi import TikTokApi
import pandas as pd

# Initialize TikTokApi instance
api = TikTokApi()

def collect_tiktok_data(hashtag, limit=100):
    # Collect TikTok data for a given hashtag
    try:
        videos = api.by_hashtag(hashtag, count=limit)
        data = [{'caption': video['desc'],
                 'duration': video['video']['duration'],
                 'sound': video['music']['title']}
                for video in videos]
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error collecting data: {e}")
        return pd.DataFrame()

# Test the function with a sample hashtag
if __name__ == "__main__":
    sample_data = collect_tiktok_data("exampleHashtag", limit=10)
    print(sample_data.head())

