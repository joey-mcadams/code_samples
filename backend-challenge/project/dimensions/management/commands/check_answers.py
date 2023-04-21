import pickle

from django.db import connection, reset_queries
from django.core.management.base import BaseCommand, CommandError

from dimensions.challenge import list_children, list_hierarchy
from dimensions.models import Company, Dimension


class Command(BaseCommand):
    help = 'Checks output of list_children() and list_hierarchy()'

    def handle(self, *args, **options):
        self.base_dir = 'dimensions/management/fixtures/'

        reset_queries()
        queries_before = len(connection.queries)

        self.check_list_children()
        children_num_queries = len(connection.queries) - queries_before
        print(f'Used {children_num_queries} queries', end='\n\n')

        self.check_list_hierarchy()
        list_hierarchy_num_queries = len(connection.queries) - children_num_queries
        print(f'Used {list_hierarchy_num_queries} queries', end='\n\n')


    def check_list_children(self):
        print('Checking list_children()...')
        with open(f'{self.base_dir}list_children_expected.pickle', mode='rb') as f:
            expecteds = pickle.load(f)

        num_correct = 0
        for dim_id, expected in expecteds.items():
            response = list_children(dim_id)
            if expected != response:
                print(f'\n Incorrect response for {expected[0]}.\n - EXPECTED: {expected}\n - RECEIVED: {response}')
            else:
                num_correct += 1

        print(f'---\nRESULTS: {num_correct} out of {len(expecteds)} correct.')

    def check_list_hierarchy(self):
        print('Checking list_hierarchy()...')
        with open(f'{self.base_dir}list_hierarchy_expected.pickle', mode='rb') as f:
            expected = pickle.load(f)

        response = list_hierarchy(1)
        if expected != response:
            print(f'\n Incorrect response.\n - EXPECTED: {expected}\n - RECEIVED: {response}\n---\nRESULTS: Fail.')
        else:
            print(f'\n{len(response)} out of {len(expected)} correct.\n---\nRESULTS: Success.')
