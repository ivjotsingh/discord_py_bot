import requests
from decouple import config


def search_query(query):
    google_url = f"https://www.googleapis.com/customsearch/v1?key={config('GOOGLE_KEY')}&" \
        f"cx={config('GOOGLE_ENGINE_ID')}&&q={query}&&num=5"
    return requests.get(google_url)