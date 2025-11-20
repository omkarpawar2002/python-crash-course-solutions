'''
 8-14. Cars: Write a function that stores information about a car in a diction
ary . The function should always receive a manufacturer and a model name . It 
should then accept an arbitrary number of keyword arguments . Call the func
tion with the required information and two other name-value pairs, such as a 
color or an optional feature . Your function should work for a call like this one:
 car = make_car('subaru', 'outback', color='blue', tow_package=True)
 Print the dictionary that’s returned to make sure all the information was 
stored correctly 
'''

def make_car(make,model,**car_info):
    build_car = {}
    build_car[make] = make
    build_car[model] = model
    for key,value in car_info.items():
        build_car[key] = value
    return build_car

car1 = make_car('odi','7x Series',color='White',seat_capacity=6)
print(car1)