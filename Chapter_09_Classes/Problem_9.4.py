'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
Add an attribute called number_served with a default value of 0 . Create an 
instance called restaurant from this class . Print the number of customers the 
restaurant has served, and then change this value and print it again .
 Add a method called set_number_served() that lets you set the number 
of customers that have been served . Call this method with a new number and 
print the value again .
 Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served . Call this method with any num
ber you like that could represent how many customers were served in, say, a 
day of business 
'''


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"RESTAURANT NAME :- {self.restaurant_name}.")
        print(f"CUISINE TYPE :- {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("Restaurant is open.")

    def set_number_served(self,customer):
        self.number_served = customer

    def increment_number_served(self,served_customers):
        self.number_served += served_customers


res_1 = Restaurant('Bikaner','Thai')
print(f"Number of customer served :- {res_1.number_served}")
res_1.number_served = 10
print(f"Number of customer served :- {res_1.number_served}")
res_1.set_number_served(190)
print(f"Number of customer served :- {res_1.number_served}")
res_1.increment_number_served(10)
print(f"Number of customer served :- {res_1.number_served}")

