#app/tests/test_models.py

'''Implement storage models and their methods.'''

from app.models import FoodOrders


class TestFoodOrders():
    '''TestFoodOrders class with storage model and methods.'''

    def set_up(self):
        '''Set up the model.'''
        self.food = FoodOrders()

    def test_get_food_orders(self):
        '''Returns an empty dictionary.'''
        assert self.food.get_food_orders() == {}
