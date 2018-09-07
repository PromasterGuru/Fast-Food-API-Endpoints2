#app/views.py

'''Implementation of API EndPoint'''

import datetime
from flask import jsonify
from flask import request
from flask import abort
from app import app
from app.models import FoodOrders

FOOD_ORDERS = FoodOrders().get_food_orders()

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

@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    '''Place a new order'''
    if not request.json or not "order_item" in request.json:
        abort(400) #Bad Request
    if not FOOD_ORDERS:
        order_id = 1
    else:
        order_id = FOOD_ORDERS[-1]['id'] + 1
    new_order = {
        "id": order_id,
        "order_item": request.json['order_item'],
        "description": request.json['description'],
        "quantity": request.json['quantity'],
	"order_date":str(datetime.datetime.now())[:19],
        "status": "Pedding"
    }
    FOOD_ORDERS.append(new_order)
    return jsonify({"Order": new_order}), 201 #Created

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

@app.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    '''Delete an order'''
    order = [order for order in FOOD_ORDERS if order['id'] == order_id]
    if not order:
        abort(404) # Not found
    FOOD_ORDERS.remove(order[0])
    return jsonify({"Result": True}), 204 #No Content
