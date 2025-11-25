'''

10-5. Programming Poll: Write a while loop that asks people why they like 
programming . Each time someone enters a reason, add their reason to a file 
that stores all the responses 

'''

while True:
    person_name = input("Enter your name :- ")
    person_choice = input("Why they like programming :- ")
    if(person_choice.lower() == 'quit'):
        break
    with open('person_choice.txt','a') as file:
        data = file.write(person_name + ' :- ' + person_choice + '\n')
