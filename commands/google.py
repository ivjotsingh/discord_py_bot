import json

from utilities.google_search import search_query
from utilities.mongo import post_to_mongo_db
from utilities.loggers import logger as log


class GoogleCommand:
    @staticmethod
    def execute(args):
        try:
            query = " ".join(args)

            # searching using google custom search API
            response = search_query(query)
            response.raise_for_status()
            response = json.loads(json.dumps(response.json()))

            # pushing search query to mongo db as log
            post_to_mongo_db({"query": f"{query}"})

            # returning list of dictionary containing description and data
            return [
                {
                    'description': item['title'],
                    'data': item['link']
                }
                for item in response['items']]
        except Exception as e:
            log.exception(msg=f'error while fetching google search results {e}')

            # returning list of dictionary containing description and data
            return [
                {
                    'description': 'Something went wrong',
                    'data': 'unable to fetch search results'
                }]
