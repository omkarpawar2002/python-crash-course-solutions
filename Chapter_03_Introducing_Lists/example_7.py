'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests .
 •	Start with your program from Exercise 3-6 . Add a new line that prints a 
message saying that you can invite only two people for dinner .
 •	Use pop() to remove guests from your list one at a time until only two 
names remain in your list . Each time you pop a name from your list, print 
a message to that person letting them know you’re sorry you can’t invite 
them to dinner .
 •	Print a message to each of the two people still on your list, letting them 
know they’re still invited .
 •	Use del to remove the last two names from your list, so you have an empty 
list . Print your list to make sure you actually have an empty list at the end 
of your program 
'''

guest_names = ['Reddica', 'Thomasan', 'Akhani', 'Sweedan', 'Edward', 'Shweta']
print("So sorry for everyone , today i will invite only 2 peoples.")
first_person = guest_names.pop()
print("I am so sorry",first_person.title(),"i can't invite them on dinner")
second_person = guest_names.pop()
print("I am so sorry",second_person.title(),"i can't invite them on dinner")
third_person = guest_names.pop()
print("I am so sorry",third_person.title(),"i can't invite them on dinner")
fourth_person = guest_names.pop()
print("I am so sorry",fourth_person.title(),"i can't invite them on dinner")

print(guest_names)
print("Hey",guest_names[0].title(),",You are still invited")
print("Hey",guest_names[1].title(),",You are still invited")

del guest_names[1]
del guest_names[0]
print(guest_names)