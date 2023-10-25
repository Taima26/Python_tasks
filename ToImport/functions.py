from ToImport.Exceptions import MealTooBig, WrongInput
import json

data = json.load(open("data.json"))
meals = data["meals"]
combos = data["combos"]

#for finding each meal and combo easly
meals_dic = {}
i=0
for i in range(len(meals)):
    meals_dic[meals[i].get("id")] = i
    i+=1

combo_dic = {}
j=0
for j in range(len(combos)):
    combo_dic[combos[j].get("id")] = j
    j+=1

#calories and price counters
def cal_counter(order):
    result = 0
    for choice in order:
        if choice in meals_dic:
            id = meals_dic[choice]
            result += meals[id].get("calories")
        elif choice in combo_dic:
            id= combo_dic[choice]
            result += cal_counter(combos[id].get("meals"))
        elif choice not in meals_dic and choice not in combo_dic:
            raise WrongInput
    if result > 2000:
        raise MealTooBig(result)
    return result

def price_counter(order):
    result = 0
    for choice in order:
        if choice in meals_dic:
            id = meals_dic[choice]
            result += meals[id].get("price")
        elif choice in combo_dic:
            id= combo_dic[choice]
            result += combos[id].get("price")
        elif choice not in meals_dic and choice not in combo_dic:
            raise WrongInput
    return result


