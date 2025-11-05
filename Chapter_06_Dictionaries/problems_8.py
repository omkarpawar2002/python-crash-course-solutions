'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet . In each dictionary, include the kind of animal and the owner’s 
name . Store these dictionaries in a list called pets . Next, loop through your list 
and as you do print everything you know about each pet 
'''

tommy = {
    'animal': 'dog',
    'owner': 'Ravi',
}

whiskers = {
    'animal': 'cat',
    'owner': 'Meera',
}

goldie = {
    'animal': 'fish',
    'owner': 'Anirudh',
}

rocky = {
    'animal': 'parrot',
    'owner': 'Kirti',
}

pets = [tommy,whiskers,goldie,rocky]
for person in pets:
    for key,value in person.items():
        print(key,'----',value)
    print()