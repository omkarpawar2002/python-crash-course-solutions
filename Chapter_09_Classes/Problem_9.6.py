'''
 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of 
the class will work; just pick the one you like better . Add an attribute called 
flavors that stores a list of ice cream flavors . Write a method that displays 
these flavors . Create an instance of IceCreamStand, and call this method 
'''

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"RESTAURANT NAME :- {self.restaurant_name}.")
        print(f"CUISINE TYPE :- {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("Restaurant is open.")
    
class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavours = ['chocklet','vanila','perry']

    def display_flavours(self):
        print("Here is a list of all flavours")
        for item in self.flavours:
            print(item.upper())

res_1 = IceCreamStand()
res_1.display_flavours()
