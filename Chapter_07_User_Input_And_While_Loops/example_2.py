'''

-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group . If the answer is more than eight, print a message say
ing they’ll have to wait for a table . Otherwise, report that their table is ready 

'''

seating_person = int(input("How many people are in there group :- "))
if(seating_person > 8):
    print("you will be wait for table!")
else:
    print("Table is ready!")