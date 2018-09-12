#app/models.py

'''Food order class with storage model and methods.'''

class FoodOrders():
    '''Food order with storage and methods.'''


    def __init__(self):
        '''Initialize food orders.'''
        self.food_orders = [
            {
                'id':1,
                'order_item':'Tater tots',
                'description': 'Pieces of deep-fried, grated potatoes served as a side dish',
                'quantity': 5,
                'order_date': '2018-09-05 13:35:42',
                'status': 'Pedding'
            },
            {
                'id':2,
                'order_item':'Cobb salad',
                'description': 'African garden salad typically made with boiled, grilled chicken breast',
                'quantity': 7,
                'order_date': '2018-09-07 14:30:22',
                'status': 'Declined'
            },
            {
                'id':3,
                'order_item':'Twinkies',
                'description': 'African Golden Sponge Cake with Creamy Filling',
                'quantity': 7,
                'order_date': '2018-09-10 14:20:17',
                'status': 'Completed'
            }
        ]

    def get_food_orders(self):
        '''Return all the food orders'''
        return self.food_orders

