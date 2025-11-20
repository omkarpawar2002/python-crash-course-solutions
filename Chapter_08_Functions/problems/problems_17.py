'''
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section 
'''

def build_profile(first,last,**user_info):
    '''Here we are creating a function which tell us about user info'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user1 = build_profile('Advait','Jadhav',age=24,location='Mumbai')
print(user1)