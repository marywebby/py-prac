# a list is a collection of items in a particular order, items in the lsit dont have to be related in any particular way either
    # square brackets indicate lists 
    # indivivdaul elements are seperated by commas 
bicycles = ['trek', 'connondale', 'redline', 'specilized']
print(bicycles)

# learn how to access individual items in a list, indexed positions start at 0, not 1(same as JS)
    # grab a single item in a list by telling python the specific [index] of the item 
print(bicycles[0])
    # tie in previous work, capitalize
print(bicycles[2].title())
    # access the last item in any list, no matter the size
print(bicycles[-1])

# using specific items from a list in a sentence 
    # using the f before a stirng = "F-string is a way to format strings in Python. 
    # It was introduced in Python 3.6 and aims to make it easier for users to add variables, 
    # comma separators, do padding with zeros and date format."
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# modifying elements in a list 
    # ex.) makinga alien shooting game, everytime an alien appears or get killed, one will be added or subtracted from a list 
    
# change the item which is inside once the list as been created 
cars = ['Jeep', 'Audi', 'Ford', 'Bronco']
print(cars)

cars[2] = 'Hummer'
print(cars)


# adding elements to a list 
    # (append)ing elements to the end of the list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

fish = []
fish.append('red snapper')
fish.append('trout')
fish.append('salmon')
print(fish)


# intserting elements into a list 
oceans = ['pacific', 'indian', 'atlantic']
print(oceans)

oceans.insert(1, 'arctic')
print(oceans)


# removing elements form a list 
colleges = ['msu', 'umich', 'wcc', 'cmu']
print(colleges)

del colleges[2]
print(colleges)


# removing an item from the list using the pop method
    # sometimes youll want ot use the value of an item after you remove it from a list 
    # for ex, getting the x and y postiion of an alien that was just shot down 
    # ex.) in a web application, removing a user from a list of actuve members to a list of inactive members.
     
pasteries = ['scone', 'croissant', 'muffin', 'donut']
print(pasteries)

    # best used if elements in th elist are used in chromological order 
popped_pastery = pasteries.pop()
print(pasteries)
print(popped_pastery)

    # popping out a specific element in a list 
best_pastery = pasteries.pop(1)
print(f"The best pastery to buy is the {best_pastery.title()}")
    # once you use pop() it is no longer in the list anymore
    

# removing an item by the value of the specific element 
print(pasteries)
pasteries.remove('scone')
print(pasteries)

    # you can also use the remove() method to work with a value thats being removed from a list 
numbers = [5, 10, 12, 15, 20]
print(numbers)

odd_one_out = 12
numbers.remove(odd_one_out)
print(numbers)
print(f"\nNumber {odd_one_out} does not follow to same pattern as the other numbers.")


# organizing a list 
    # sorting a list permanently with the sort() method
    # want to sort things aplhabetically 
planets = ['marcury', 'earth', 'mars', 'venus', 'pluto', 'saturn', 'uranus']
# planets.sort()
# print(planets)
    # try it in reverse order now 
planets.sort(reverse=True)
# print(planets)

# sorting a list temporarily with sort() method
print(f"\nHere is the original list: \n{planets}")

print("\nHere is the sorted list:")
print(sorted(planets))

print("\nHere is the original list again:")
print(planets)

# printing a list in reverse order 
print(planets)
planets.reverse()
print(planets)

# finding the length of a list  
    # using the len() function 
print(planets)
num_of_planets = len(planets)
print(num_of_planets)
    # this is particulary helpful when you need to identify the number of aliens that sitll need ot be shot down in a game


# avoiding index errors when working with lists 
singer = "mariah"
message = (f"my favorite singer is {singer.title()}.")
print(message)