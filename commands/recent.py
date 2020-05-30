from utilities.mongo import fetch_from_mongo_db


class RecentCommand():

    @staticmethod
    def execute(args):
        query = " ".join(args)
        results = ", ".join(fetch_from_mongo_db(query))

        return [{
                'heading': f'Recent Searches for {query}',
                'content': results}
            ]
