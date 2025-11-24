'''
9-3. Users: Make a class called User . Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile . Make a method called describe_user() that prints a summary 
of the user’s information . Make another method called greet_user() that prints 
a personalized greeting to the user .
 Create several instances representing different users, and call both methods 
for each user 
'''

class User:
    def __init__(self,first,last,location,age):
        self.first_name = first
        self.last_name = last
        self.location = location
        self.age = age

    def describe_user(self):
        print(f"FIRST NAME :- {self.first_name.title()}\nLAST NAME :- {self.last_name.title()}\nLOCATION :- {self.location.title()}\nAGE :- {self.age}.")
    
    def greet_user(self):
        print(f"Welcome {self.first_name.upper()}, Thank you for comming.")

user1 = User('john','doe','washington DC',32)
user1.describe_user()
user1.greet_user()
print()
user2 = User('Ashok','Tiwari','Mumbai',29)
user2.describe_user()
user2.greet_user()