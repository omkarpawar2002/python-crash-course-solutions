'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . 
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people . Loop through your list of people . As you 
loop through the list, print everything you know about each person 
'''

person1 = {
    'first_name': 'Anirudh',
    'last_name': 'Sharma',
    'age': 28,
    'city': 'Kolkata',
}

person2 = {
    'first_name': 'Meera',
    'last_name': 'Iyer',
    'age': 34,
    'city': 'Chennai',
}

person3 = {
    'first_name': 'Ravi',
    'last_name': 'Patel',
    'age': 41,
    'city': 'Ahmedabad',
}

people = [person1,person2,person3]

for person in people:
    for key,value in person.items():
        print(key,'----',value)
    print()
