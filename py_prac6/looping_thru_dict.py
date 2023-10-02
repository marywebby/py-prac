# looping through dictionaries for key and values
    # lets try a dictionary where their store information about a persons profile 
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
    # say you want to access all pieces of info in this ditcionary, not just a specific piece 
    # we can use a for loop
for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")
    # can use any names for key and value, such as k and v if we like 
    # this type of looping through information is really good if you want to display information that is similar
    # such as favorite languages in the dicitonaries file 
    # for example 
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"\n{name}'s favorite language is {language}!")
    
    
# looping through for all the keys in a dictionary  
    # the keys() method is useful when you dont need to work with all of the values in a dictionary
    # lets loop through fav langues just to see everyone who took the poll
for name in favorite_languages.keys():
    print(f"\n{name}")
    # looping through keys is actually the defualy for whe you do `for x in x_dict():`

    # now lets print a message for our friends
    # say we want to print just two of our friends names as it loops through our dicitonary 
    # we will give it the names and when it matches it will print those
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love{language}!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")
    

# looping through a dictiionarys keys in a particular order 
    # looping outputs keys and values in the order they were inserted,
    # say you want to loop through in a different order 
    # if you want the keys to be sorted as they are returned from the for loop 
    # this is where we use .sort()
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")
    # this for statement is like the others, expect we wrapped the sorted() function around the dic.keys()
    # this tells python to get all the keys in the dict and sort them before starting the loop.
    # displayed the names in order 
    
    
# looping through all values in a dictionary 
    # if you are only interested in the values, you can use .values()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    # printing these prints all the values including repeats
    # to print unique values, we can use set()
for language in set(favorite_languages.values()):
    print(language.title())
    # you can build a set directly by using braces and seperating the elements with commas
    # languages = {'c', 'python', 'rust', 'c'}
    # languages
    # {'c', 'python', 'rust'}
    