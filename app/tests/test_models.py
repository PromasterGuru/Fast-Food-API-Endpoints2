#app/tests/test_models.py

'''Implement storage models and their methods'''

import unittest
from app.models import FoodOrders

class TestModelCases(unittest.TestCase):
    '''TestFoodOrders class with storage model and methods'''

    def setUp(self):
        '''Set up the model.'''
        self.food = FoodOrders()

    def test_class_inits_with_some_records(self):
        '''The model intializes with some records'''
        result = self.food.get_food_orders()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
