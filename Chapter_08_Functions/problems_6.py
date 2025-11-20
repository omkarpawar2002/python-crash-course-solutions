'''
8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country . The function should return a string formatted like this:
 "Santiago, Chile"
 Call your function with at least three city-country pairs, and print the value 
that’s returned 
'''

def city_country(city,country):
    return f'"{city.title()},{country.title()}"'

first_country = city_country('mumbai','india')
print(first_country)
second_country = city_country('Washinton DC','usa')
print(second_country)
third_country = city_country('karachi','pakistan')
print(third_country)
