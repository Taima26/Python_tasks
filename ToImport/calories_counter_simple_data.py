from ToImport.Exceptions  import MealTooBig, WrongInput
calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

def cal_cntr(choices):
    result = 0
    for choice in choices:
        if choice in calories:
            result += calories[choice]
        elif choice in combos:
            result += cal_cntr(combos[choice])
        else:
            return f"sorry we don't have {choice} on the menue"
    if result > 2000:
        return f"your meal is too big, {result} is bigger than 2000!"
    return result




