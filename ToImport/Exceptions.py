class MealTooBig (Exception):
    def __init__(self, calories):
        self.message = f"Meal is too big! {calories} exceed 2000!"
        super().__init__(self.message)