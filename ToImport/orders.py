from datetime import datetime
from ToImport.Exceptions import MealTooBig, WrongInput
from ToImport.functions import cal_counter, price_counter

class Order:
    counter=0
    def __init__(self, items , date=None):
        self.items = items
<<<<<<< HEAD
        if date == None:
            self.date = datetime.now()
        else:
            self.date = date
=======
        self.date = datetime.now()
>>>>>>> de4e7bf77e509910915a4f5d3708bf4712662126
        self.order_id = f"order-{Order.counter}"
        Order.counter +=1
        self.order_accepted = self.is_order_accepted()
        self.order_refuse_reason = str
        self.calories = self.order_calories
        self.price = self.order_price
   
    def is_order_accepted(self):
        try:
            cal_counter(self.items)
            return True
        except Exception as e:
            self.order_refuse_reason = e
            return False

    @property   
    def order_calories(self):
        if self.order_accepted:
            return cal_counter(self.items)
            
    @property
    def order_price(self):
        if self.order_accepted:
            return price_counter(self.items)
        