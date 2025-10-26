'''
 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60) . Make a copy of the list of pizzas, and call it friend_pizzas . 
Then, do the following:
 •	Add a new pizza to the original list .
 •	Add a different pizza to the list friend_pizzas .
 •	Prove that you have two separate lists . Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list . Print the message, 
My friend’s favorite pizzas are:, and then use a for loop to print the sec
ond list . Make sure each new pizza is stored in the appropriate list 
'''

my_pizza = ['mashroom','pepproni','masala tadka']
friend_pizza = my_pizza[:]
my_pizza.append("Masai Neun")
friend_pizza.append("Kunai cheruku")
print("My Favourite Pizza Are :- ")
for pizza in my_pizza:
    print(pizza.title())
    
print()

print("My Friends Favourite Pizza are :- ")
for pizza in friend_pizza:
    print(pizza.title())