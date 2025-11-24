'''
9-7. Admin: An administrator is a special kind of user . Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on . 
Write a method called show_privileges() that lists the administrator’s set of 
privileges . Create an instance of Admin, and call your method 
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

class Admin(User):
    def __init__(self):
        self.privileges = ["Can add post","Can delete post","Can ban user"]

    def show_privileges(self):
        for i in self.privileges:
            print(i)

a1 = Admin()
a1.show_privileges()