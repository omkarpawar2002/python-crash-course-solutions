'''
 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations . You’ll have to think of 
someone else to invite .
 •	Start with your program from Exercise 3-4 . Add a print statement at the 
end of your program stating the name of the guest who can’t make it .
 •	Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting .
 •	Print a second set of invitation messages, one for each person who is still 
in your list 
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