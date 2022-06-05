import json

my_pizza_name = str(input("What pizza would you like: "))
my_pizza_ingredients = str(input("What ingredients do you want "))
ingredients = my_pizza_ingredients.split()

custom_pizza = {"pizza_name" : my_pizza_name, "ingredients" : ingredients}

print(custom_pizza)

filename = "menu_pizze.json"

with open(filename, 'r+') as f:
   
    x = json.load(f)
    x.append(custom_pizza)
    f.seek(0)
    json.dump(x, f)
            
                          
                  