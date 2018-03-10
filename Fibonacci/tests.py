from django.test import TestCase
import unittest
from django.test import Client
# Create your tests here.
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/Fibonacci/12/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        print response.content
        # Check that the rendered context contains 5 customers.
        self.assertEqual(response.content, '1')

