'''

5-2. More Conditional Tests: You don’t have to limit the number of tests you 
create to 10 . If you want to try more comparisons, write more tests and add 
them to conditional_tests.py . Have at least one True and one False result for 
each of the following:
 •	Tests for equality and inequality with strings
 •	Tests using the lower() function
 •	Numerical tests involving equality and inequality, greater than and 
less than, greater than or equal to, and less than or equal to
 •	Tests using the and keyword and the or keyword
 •	Test whether an item is in a list
 •	Test whether an item is not in a list
 
 '''


# This is for an equality check 
'''
name = "kartika"
if(name == 'kartika'):
    print("User match!")
'''

# This is for an inequality checks 
'''
age = 20
if(age != 21):
    print("Age not Match!")
'''

# Check some relational operators > < >= <=
'''
age = 21
if(age > 18):
    print("You are eligible to vote")
if(age < 18):
    print("You are not enough to vote")
if(age >= 18):
    print("Just 2 months ago you eligible for an vote")
if(age <= 18):
    print("Not eligible")
'''

# Test using and keyword and or keyword
'''
age = 23
if(age > 18 and age < 24):
    print("You are eligible for donating blood")
if(age < 18 and age > 65):
    print("You are not eligible for donating blood")

name = "suchita"
if(name == 'suchita' or name == 'vamika'):
    print("Correct userName")
if(name == 'sushant' or name == 'suchita'):
    print("Again Match")
'''

# now we are testing whether the item is in list or not 

li = [10,20,30,40,50]
if(10 in li):
    print("Yes it is present in list")
if(1000 not in li):
    print("Yes it is also not in list")