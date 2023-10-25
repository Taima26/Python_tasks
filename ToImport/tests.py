from unittest import TestCase
from ToImport.functions import cal_counter, price_counter
from ToImport.Exceptions import MealTooBig, WrongInput

class Test_cal_and_price_counters(TestCase):
    def test_count_meals(self):
        result = cal_counter(["meal-1", "meal-2","meal-3"])
        assert result == 1750
    
    def test_count_combos(self):
        result = cal_counter(["combo-1", "combo-2"])
        assert result == 1770

    def test_price_counter(self):
        result = price_counter(["meal-1", "combo-2"])
        assert result == 15

    def test_big_meal_exception(self):
        with self.assertRaises(MealTooBig) as e:    
            cal_counter(["combo-1", "combo-2", "combo-2"])    
        assert e.exception.message == "Meal is too big! 2470 exceed 2000!"
    
    def test_wrong_input(self):
        with self.assertRaises(WrongInput) as e:
            cal_counter(["combo-1", "combo-2", "combo-15"])
        assert e.exception.message == '''Sorry,"combo-15" isn't on the menue'''
