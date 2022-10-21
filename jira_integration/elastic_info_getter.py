from elasticsearch import Elasticsearch
from dateutil import parser
import time


class ElasticInfoGetter():
    def __init__(self):
        self.elastic_client = Elasticsearch("http://localhost:9200")

    def get_documents_from_the_last_hour(self):
        # result.body['hits']['hits'][0]['_source']['fields']['priority']['name']

        query_body = {
            "from": 0,
            "size": 10000,
            "query": {
                "bool": {
                    "must": {"match_all": {}},
                    "filter": [{
                        "range": {
                            "fields.created": {
                                "gte": "now-1h"
                            }
                        }
                    }]
                }
            }
        }

        results = self.elastic_client.search(index="jira_tickets", body=query_body)
        return results.body['hits']['hits']

    def get_all_indexes(self):
        return self.elastic_client.indices.get_alias()

    def convert_to_epoch(self, ticket: dict) -> int:
        iso_time = ticket['_source']['fields']['created']
        return int(parser.parse(iso_time).timestamp())

    def get_array_of_hits_per_minute(self):
        num_hits_array = []
        now = int(time.time())
        then = now - 3600
        increment = 60

        all_tickets = self.get_documents_from_the_last_hour()

        while now > then:
            current_number_of_hits = 0
            for ticket in all_tickets:
                time_created = self.convert_to_epoch(ticket)
                if then < time_created <= then + increment:
                    current_number_of_hits += 1

            num_hits_array.append(current_number_of_hits)
            then += increment

        return num_hits_array


