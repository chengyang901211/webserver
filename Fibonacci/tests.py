from django.test import TestCase
import unittest
from django.test import Client
# Create your tests here.
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_regular_get_method(self):
        # Issue a GET request.
        response = self.client.get('/Fibonacci/5/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_regular_post_method(self):
        # Issue a post request.
        response = self.client.post('/Fibonacci/5/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 405)

    def test_regular_put_method(self):
        # Issue a put request.
        response = self.client.put('/Fibonacci/5/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 405)

    def test_edge_case(self):
        #Edge case for first 0 Fibonacci numbers
        response = self.client.get('/Fibonacci/0/')
        #Expect '[]' as return
        self.assertEqual(response.content, '[]')

    def test_base_case(self):
        #base_ case for first 1 Fibonacci numbers
        response = self.client.get('/Fibonacci/1/')
        #Expect '[0]' as return
        self.assertEqual(response.content, '[0]')
        #Edge case for first 0 Fibonacci numbers
        response = self.client.get('/Fibonacci/2/')
        #Expect '[0,1]' as return
        self.assertEqual(response.content, '[0,1]')

    def test_general_input(self):
        #first 5 Fibonacci numbers
        response = self.client.get('/Fibonacci/5/')
        #Expect
        self.assertEqual(response.content, '[0,1,1,2,3]')

        #first 7 Fibonacci numbers
        response = self.client.get('/Fibonacci/7/')
        #Expect
        self.assertEqual(response.content, '[0,1,1,2,3,5,8]')

    def test_invalid_input(self):
        #Invalid negative input
        response = self.client.get('/Fibonacci/-5/')
        #Expect return http 400
        self.assertEqual(response.status_code, 400)
