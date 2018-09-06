#app/views.py

'''Implementation of API EndPoint'''

import datetime
from flask import jsonify
from flask import request
from flask import abort
from app import app
from app.models import FoodOrders

FOOD_ORDERS = FoodOrders().get_food_orders()

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
        "order_date": str(datetime.datetime.now())[:19],
        "status": "False"
    }
    FOOD_ORDERS.append(new_order)
    return jsonify({"Order": new_order}), 201 #Created
