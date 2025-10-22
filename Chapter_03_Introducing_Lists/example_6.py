'''
3-6. More Guests: You just found a bigger dinner table, so now more space is 
available . Think of three more guests to invite to dinner .
•	Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print 
statement to the end of your program informing people that you found a 
bigger dinner table .
•	Use insert() to add one new guest to the beginning of your list .
•	Use insert() to add one new guest to the middle of your list .
•	Use append() to add one new guest to the end of your list .
•	Print a new set of invitation messages, one for each person in your list 
'''

guest_names = ["Thomasan","Syndrella","Edward"]
print("Hello",guest_names[0].upper(),",Please enjoy your party!")
print("Hello",guest_names[1].upper(),",Please enjoy your party!")
print("Hello",guest_names[2].upper(),",Please enjoy your party!")

print("Sorry Guys,",guest_names[1].upper(),"will not be able to join the party!")

guest_names[1] = "Sweedan"
print("Hello",guest_names[0].upper(),",Please enjoy your party!")
print("Hello",guest_names[1].upper(),",Please enjoy your party!")
print("Hello",guest_names[2].upper(),",Please enjoy your party!")

print("Hello Everyone tomorrow we found the big dinner table!")

guest_names.insert(0,'Reddica')
guest_names.insert(2,'Akhani')
guest_names.append('Shweta')

print("Hello",guest_names[0].upper(),",Please enjoy your party!")
print("Hello",guest_names[1].upper(),",Please enjoy your party!")
print("Hello",guest_names[2].upper(),",Please enjoy your party!")
print("Hello",guest_names[3].upper(),",Please enjoy your party!")
print("Hello",guest_names[4].upper(),",Please enjoy your party!")
print("Hello",guest_names[5].upper(),",Please enjoy your party!")
