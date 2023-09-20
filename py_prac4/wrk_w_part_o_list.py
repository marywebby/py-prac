# working with a part of a list 
    # called slice 

# slicing a list
    # to make a slice, you specify the index of the first and last elements you want to work with. 
    # just like in range(), python stops one index before the specified index, to output the first 3 elements in a list
    # you would request indices 0 through 3, whcih would return elements 0,1,2
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'mary']
print(players[0:3])
print(players[1:4])

    # omitting the first index will automatically start your splice at the beinging of the list 
print(players[:4])
    # omitting the last number will finish the list starting at the number given 
print(players[2:])
    # will start at the 3rd from the last element, in this case florence
print(players[-3:])

# looping through a slice 
    # use a slice in a for loop to loop through a subset of the lements in a list.
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    # could be used for a scoreboard to loop through the names at the top of the board. 
    
# copying a list 
    # make a new list based off a previous list 
    # you make a new list by [:], this tells python to make a brand new list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

    # to prove that they are two seperate lists we will add a new food to each one 
    # place above the prints to make sure that the new food is added
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)




