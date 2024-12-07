from dotenv import load_dotenv
import requests
import os
from random import choice

load_dotenv()

news_api_url = os.getenv("NEWS_API_URL")
news_api_key = os.getenv("NEWS_API_KEY")

params = {"country": "tr", "tag": "general"}
headers = {"content-type": "application/json", "authorization": news_api_key}


def fetch_news(tag="general"):
    category_list = [
        "general",
        "sport",
        "technology",
        "health",
        "entertainment",
    ]
    if tag == "random":
        tag = choice(category_list)
    try:
        response = requests.get(
            news_api_url,
            headers=headers,
            params=[("country", "tr"), ("tag", tag)],
        )
        data = response.json()
        news = data["result"]
        return news
    except Exception as e:
        print(e)
