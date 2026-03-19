import requests

APIFY_TOKEN = "YOUR_APIFY_TOKEN"

def fetch_leads(hashtag):
    url = f"https://api.apify.com/v2/acts/apify/instagram-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"

    payload = {
        "hashtags": [hashtag],
        "resultsLimit": 20
    }

    response = requests.post(url, json=payload)
    data = response.json()

    leads = []

    for item in data:
        leads.append({
            "username": item.get("username"),
            "bio": item.get("biography"),
            "followers": item.get("followersCount"),
            "engagement": item.get("engagementRate"),
            "recent_post": (item.get("latestPosts") or [{}])[0].get("caption")
        })

    return leads
    import os
from dotenv import load_dotenv

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
