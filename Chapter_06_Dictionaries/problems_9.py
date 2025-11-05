'''
6-9. Favorite Places: Make a dictionary called favorite_places . Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person . To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places . Loop through the dictionary, and print 
each person’s name and their favorite places 
'''

favorite_places = {
    'rohit':['Mumbai','Delhi','Pune'],
    'anita':['Goa','Raygad'],
    'Arun':['kanyakumari','tajmahal']
}

for name,places in favorite_places.items():
    print("Hey i'm",name.title())
    print("Here are my fovourite places are :- ")
    for place in places:
        print(place.title())
    print()