import json

class Pizza:
    
    def __init__(self, name, ingredients):
        
        self.name = name
        self.ingredients = ingredients
        
    def print_ingredients(self):
        
        print(f"Gli ingredienti della {self.name} sono:")
        
        for ingredient in self.ingredients:
            
            print(ingredient)
            
class Menu:
    
    def __init__(self):
        
        self.pizze_list = []
        
    def add_pizza(self, pizza: Pizza):
        
        self.pizze_list.append(pizza)
        
    def show_menu(self):
        
        for pizza in self.pizze_list:
            index = self.pizze_list.index(pizza)+1 
            print(f"\n{str(index)}: {pizza.name} ")
            pizza.print_ingredients()      
            
    def read_menu(self, filename): 

        with open(filename) as f:
            menu = json.load(f)
   
            for pizzajson in menu:

                pizza_obj= Pizza(pizzajson["pizza_name"], pizzajson["ingredients"])
                self.add_pizza(pizza_obj)
                
class Basket:
    
    def __init__(self):    
        self.pizze = []
        self.user_input = -1
        
    def order_pizza(self, menu: Menu):
        print("To order press the corrispondent pizza number")
        print("To finish the order press 0")
        while self.user_input != 0:
            self.user_input = int(input("What pizza do you want? "))
            
            if self.user_input > 0:
                name = menu.pizze_list[self.user_input-1].name
                number_pizza = int(input(f"How many {name} do you want? "))
                self.pizze.append({'pizza_name': name , 'quantity': number_pizza})
    
        print("Thank you for your order, you have:")
    
        for pizza in self.pizze:
    
            print(str(pizza['quantity']) + "x " + pizza['pizza_name']) 
            
            

my_menu = Menu()
my_basket = Basket()

my_menu.read_menu("menu_pizze.json")
my_menu.show_menu()  
my_basket.order_pizza(my_menu)



    
