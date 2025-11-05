'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers . 
Think of five names, and use them as keys in your dictionary . Think of a favorite 
number for each person, and store each as a value in your dictionary . Print 
each person’s name and their favorite number . For even more fun, poll a few 
friends and get some actual data for your program 
'''

favourite_number = {
    'Kerry':34,
    'Virat':18,
    'Dhoni':7,
    'Rohit':45,
    'Sachin':1,
}
for name,number in favourite_number.items():
    print(f"{name.title()}'s Favourite Number is :- {str(number)}")