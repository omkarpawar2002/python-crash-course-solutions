'''
7-10. Dream Vacation: Write a program that polls users about their dream 
vacation . Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll 
'''

user_responses = {}

polling_active = True
while polling_active:
    name = input("Enter your name :- ")
    place = input("If you could visit one place in the world,where would you go ?")
    user_responses[name] = place
    repeat = input("Do you want to add other person responses :- yes or no ")
    if(repeat == 'no'):
        polling_active = False
print()
print("Here is the person responses")
for name , place in user_responses.items():
    print(f"{name.title()} want to visit :- {place.title()}")