import requests

class RealTimeFetcher:
    def __init__(self, news_api_key):
        self.news_api_key = news_api_key

    def fetch_news_articles(self, topic, max_results=5):
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={self.news_api_key}&pageSize={max_results}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [
                {
                    "title": article["title"],
                    "description": article["description"],
                    "url": article["url"]
                }
                for article in data.get("articles", [])
            ]
        return []
