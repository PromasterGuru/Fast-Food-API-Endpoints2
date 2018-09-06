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

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    '''Get all the orders.'''
    return jsonify({"Orders": FOOD_ORDERS}), 200 #OK

@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    '''Fetch a specific order'''
    order = [order for order in FOOD_ORDERS if order['id'] == order_id]
    if not order:
        abort(404) #Not Found
    return jsonify({"Order": order}), 200 #OK

@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    '''Fetch a specific order'''
    order = [order for order in FOOD_ORDERS if order['id'] == order_id]
    if not order:
        abort(404) #Not Found
    return jsonify({"Order": order}), 200 #OK

@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    '''Update the status of an order.'''
    if (not request.json or not "status" in request.json):
        abort(400) #Bad Request
    order = [order for order in FOOD_ORDERS if order['id'] == order_id]
    if not order:
        abort(404) # Not found
    order[0]['status'] = request.json['status']
    return jsonify({"Order": order}), 202 #Accepted
