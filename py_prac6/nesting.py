# nesting
    # sometimes youll want to store multiple dict in a list, or a list of itmes as a value in a dict. 
 
 
 
    
# A LIST OF DICTIONARYS
    # alien_0 dict contains a variety of information about one alien, but has no room to store info about a 2nd
    # how can you manage a fleet of aliens? 
    # one way is to make a list of aliens in which each alien is a dictionary of info about that alien 
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
    # more realistic example would involve more than 3 aliens with code that auto generates each alien
    # we can use range() to create a fleet of 30 aliens 
# make an empty list for storing aliens
aliens = []

# make 30 green aliens 
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]: 
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens 
for alien in aliens[:5]:
    print(alien)
print("...")
# show how many aliens have been created
print(f"total number of aliens: {len(aliens)}")

    # this could work well if the aliens change characteristics throughout the game 
    # say as they get closer they become yellow and medium speed and 10 points 
# placed changes on line 27
# can also add an elif, in which it changes yellow to red





# A LIST IN A DICTIONARY 
    # rather than putting a dictionary inside a list, we can put a list inside a dictionary
    # say some1 is ordering a pizza, if you were using a list, all you could store is the pizza toppings
    # with a dictionary, a list of toppings can be just one aspect of the pizza you describe 
    # two kinds of info, crust flavor and toppings. 
    # toppings values are associated with key 'toppings'
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# summarize order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
    
    # you can nest a list inside a dictionary anytime i want to have more than one value for a key 




# A DICTIONARY IN A DICTIONARY
    # you can nest a dictionary inside another dictionary, but the code can get messy quick
    # for ex, if you want to store multi users of a website 
    # you can make a dict of users, and label their dict inside with their name
    # 
users = {
    'aeinstien' : {
        'first': 'albert',
        'last': 'einstien', 
        'location': 'princeton'
    }, 
    'mcurie' : {
        'first': 'marie',
        'last': 'curie', 
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = (f"{user_info['first']} {user_info['last']}")
    location = user_info['location']
    
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")