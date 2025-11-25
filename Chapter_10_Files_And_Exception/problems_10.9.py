'''

 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
silently if either file is missing

'''

# here just assume i also have new_cats.txt file on other location okk 

try:
    with open('new_cats.txt','r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    pass