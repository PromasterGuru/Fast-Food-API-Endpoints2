#app/tests/test_views.py

'''Implement classes and methods for testing API Endpoints.'''

import json
import unittest
import datetime
from app import app

class RouteTestCases(unittest.TestCase):
    '''This class represents the orders test cases'''

    def setup(self):
        '''Define variables and initialize app'''
        self.client = app.test_client
        self.order = {
            'id': 1,
            'order_item': 'Tater tots',
            'description': 'These are Pieces of deep-fried, potatoes.',
            'quantity': 7,
            'order_date': str(datetime.datetime.now())[:19],
            'status': 'Accepted'
        }

    def test_user_can_place_an_order(self):
        '''Test API can create a new order (POST request)'''
        resp = self.client().post('/api/v1/orders', data=self.order)
        self.assertEqual(resp.status_code, 201)
        self.assertIn('Tater tots', str(resp.data))

    def test_user_can_get_all_orders(self):
        '''Test API can return all the orders (GET request)'''
        resp = self.client().post('/api/v1/orders', data=self.order)
        self.assertEqual(resp.status_code, 201)
        resp = self.client().get('/api/v1/orders')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Tater tots', str(resp.data))

    def test_user_can_fetch_a_specific_order(self):
        '''Test API can return a specific order using its id (GET request)'''
        resp = self.client().post('/api/v1/orders', data=self.order)
        self.assertEqual(resp.status_code, 201)
        result_in_json = json.loads(resp.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/api/v1/orders/{}'.format(result_in_json['id']))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Tater tots', str(result.data))
