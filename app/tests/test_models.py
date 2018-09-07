#app/tests/test_models.py

'''Implement storage models and their methods'''

import unittest
from app.models import FoodOrders

class TestModelCases(unittest.TestCase):
    '''TestFoodOrders class with storage model and methods'''

    def setup(self):
        '''Set up the model.'''
        self.food = FoodOrders()

    def test_class_inits_with_empty_list(self):
        '''Returns an empty list'''
        self.assertFalse(self.food.food.get_food_orders())
