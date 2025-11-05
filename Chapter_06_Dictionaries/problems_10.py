'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number . Then print each person’s 
name along with their favorite numbers 
'''


favourite_number = {
    'Kerry':[45,67,34],
    'Virat':[13,56,6,34,34],
    'Dhoni':[7,14],
    'Rohit':[45],
    'Sachin':[34,56,23],
}
for name,numbers in favourite_number.items():
    print("My name is :- ",name.title())
    print("My favourite numbers are ")
    for number in numbers:
        print(number)
    print()