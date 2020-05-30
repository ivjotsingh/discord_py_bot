import requests
from decouple import config


class GoogleCommand:
    @staticmethod
    def execute(message, args):
        query = " ".join(args)

        google_url = f"https://www.googleapis.com/customsearch/v1?key={config('GOOGLE_KEY')}&" \
            f"cx={config('GOOGLE_ENGINE_ID')}&&q={query}&&num=5"
        response = requests.get(google_url).json()
        response.raise_for_status()

        for data in response.items:
            print(data)

