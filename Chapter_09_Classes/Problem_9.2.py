'''
9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three 
different instances from the class, and call describe_restaurant() for each 
instance 
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

res_1 = Restaurant('Bikaner','Thai')
res_1.describe_restaurant()
print()
res_2 = Restaurant('Amrut-tulya','Veg')
res_2.describe_restaurant()
print()
res_3 = Restaurant('Anupama','Chinese')
res_3.describe_restaurant()

