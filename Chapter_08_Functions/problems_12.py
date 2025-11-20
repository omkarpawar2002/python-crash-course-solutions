'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants 
on a sandwich . The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the sand
wich that is being ordered . Call the function three times, using a different num
ber of arguments each time 
'''

def make_sandwich(*toppings):
    print("Here is the list of all the items person want to put on sandwich")
    for topping in toppings:
        print("Adding :- ",topping.upper())
    print()

make_sandwich('pepproni')
make_sandwich('pepproni','green cheepers','green chilli')

