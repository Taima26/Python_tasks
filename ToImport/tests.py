from unittest import TestCase
from ToImport.functions import cal_counter, price_counter
from ToImport.Exceptions import MealTooBig

class Test_cal_counter(TestCase):
    def test_count_meals(self):
        result = cal_counter(["meal-1", "meal-2","meal-3"])
        assert result == 1750
    
    def test_count_combos(self):
        result = cal_counter(["combo-1", "combo-2"])
        assert result == 1770

    def test_price_counter(self):
        result = price_counter(["meal-1", "combo-2"])
        assert result == 15

    def test_Big_meal(self):
        result = cal_counter (["combo-1", "combo-1", "combo-1", "combo-1"])
        assert result == MealTooBig