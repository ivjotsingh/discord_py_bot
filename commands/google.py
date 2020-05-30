import requests
from decouple import config
import json


class GoogleCommand:
    @staticmethod
    def execute(message, args):
        query = " ".join(args)

        # using custom search Rest API of google to get top 5 results
        google_url = f"https://www.googleapis.com/customsearch/v1?key={config('GOOGLE_KEY')}&" \
            f"cx={config('GOOGLE_ENGINE_ID')}&&q={query}&&num=5"
        response = requests.get(google_url)
        response.raise_for_status()

        response = json.loads(json.dumps(response.json()))

        # returning list of dictionary containing heading and content
        return [
            {
                'heading': item['heading'],
                'content': item['content']
            }
            for item in response['items']]