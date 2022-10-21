from unittest import TestCase
import elastic_info_getter

class TestElasticInfoGetter(TestCase):
    def setUp(self) -> None:
        self.test_class = elastic_info_getter.ElasticInfoGetter()

    def test_get_high_and_higher_over_the_last_hour(self):
        result = self.test_class.get_documents_from_the_last_hour()
        self.assertIsNotNone(result)

    def test_get_all_indexes(self):
        result = self.test_class.get_all_indexes()
        self.assertIsNotNone(result)

    def test_convert_to_epoch(self):
        test_ticket = {"_source": {"fields": {"created": "2022-10-19T16:16:43.803-0500"}}}
        result = self.test_class.convert_to_epoch(test_ticket)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, int)
        # '2022-10-19T16:16:43.803-0500'
        # result[1]['_source']['fields']['created']

    def test_get_array_of_hits_per_minute(self):
        result = self.test_class.get_array_of_hits_per_minute()
        self.assertIsNotNone(result)