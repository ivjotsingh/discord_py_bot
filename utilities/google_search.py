import requests
from decouple import config


def search_query(query):
    no_of_results = config('NO_OF_GOOGLE_RESULTS')
    google_url = f"https://www.googleapis.com/customsearch/v1?key={config('GOOGLE_KEY')}&" \
        f"cx={config('GOOGLE_ENGINE_ID')}&&q={query}&&num={no_of_results}"
    return requests.get(google_url)