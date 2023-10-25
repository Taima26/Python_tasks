from datetime import datetime
from ToImport.Exceptions import MealTooBig, WrongInput
from ToImport.functions import cal_counter, price_counter

class Order:
    counter=0
    def __init__(self, items , date=None):
        self.items = items
        self.date = datetime.now()
        self.order_id = f"order-{Order.counter}"
        Order.counter +=1
        self.order_accepted = self.is_order_accepted()
        self.order_refuse_reason = str
        #self.calories = self.calories_property()
        #self.price = self.price_property()
   
    def is_order_accepted(self):
        try:
            cal_counter(self.items)
            return True
        except Exception as e:
            self.order_refuse_reason = e
            return False

    @property   
    def calories_property(self):
        if self.order_accepted:
            return cal_counter(self.items)
            
    @property
    def price_property(self):
        if self.order_accepted:
            return price_counter(self.items)
        