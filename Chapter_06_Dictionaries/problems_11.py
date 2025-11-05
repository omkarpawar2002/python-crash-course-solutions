'''
6-11. Cities: Make a dictionary called cities . Use the names of three cities as 
keys in your dictionary . Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city . The keys for each city’s dictionary should be something like 
country, population, and fact . Print the name of each city and all of the infor
mation you have stored about it
'''

cities = {
    'mumbai':{
        'country':'bharat',
        'population':'1.2 Billion',
        'fact':'Mumbai is a heart of Bharat'
    },
    'new_york': {
        'country': 'USA',
        'population': '8.5 Million',
        'fact': 'New York is known as the city that never sleeps'
    },
    'karachi': {
        'country': 'Pakistan',
        'population': '15 Million',
        'fact': 'Karachi is the largest city and economic hub of Pakistan'
    },
}

for city,city_info in cities.items():
    print('\n')
    print(city.title())
    print("Here we can see some fact about ",city.title())
    for key,value in city_info.items():
        print(key,':- \n\t',value)
    print()