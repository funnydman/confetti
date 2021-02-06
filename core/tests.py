from django.test import Client
from django.test import TestCase


class ExampleTestCase(TestCase):
    def test_index_page(self):
        c = Client()
        resp = c.get('/')
        self.assertEqual(resp.status_code, 200)
