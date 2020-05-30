from utilities.mongo import fetch_from_mongo_db
from utilities.loggers import logger as log


class RecentCommand:

    @staticmethod
    def execute(args):
        try:
            query = " ".join(args)

            # fetching history from mongo db
            results = ", ".join(fetch_from_mongo_db(query))

            # returning list of dictionary containing description and data to be rendered on discord
            return [{
                    'description': f'Recent Searches for {query}',
                    'data': results
                    }]

        except Exception as e:
            log.exception(msg=f'error while fetching google search results {e}')

            # returning list of dictionary containing description and data to be rendered on discord
            return [
                {
                    'description': 'Something went wrong',
                    'data': 'unable to fetch history'
                }]
