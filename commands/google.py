import json

from utilities.google_search import search_query
from utilities.mongo import post_to_mongo_db


class GoogleCommand:
    @staticmethod
    def execute(args):
        # todo add logging and exception handling

        query = " ".join(args)
        response = search_query(query)
        response.raise_for_status()

        response = json.loads(json.dumps(response.json()))

        # returning list of dictionary containing heading and content
        post_to_mongo_db({"query": f"{query}"})

        return [
            {
                'description': item['title'],
                'data': item['link']
            }
            for item in response['items']]