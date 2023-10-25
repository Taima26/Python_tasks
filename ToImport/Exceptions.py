class MealTooBig (Exception):
    def __init__(self, calories):
        self.message = f"Meal is too big! {calories} exceed 2000!"
        super().__init__(self.message)

class WrongInput (Exception):
    def __init__(self, choice):
        self.message = f'''Sorry,"{choice}" isn't on the menue'''
        super().__init__(self.message)