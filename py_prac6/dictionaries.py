# dictionaries 

# a simple dictionaries
    # consider an alien game, they have different colors and point values, a dictionary would store this information 
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# working with dictionaries
    # defined by a collection of key value pairs
    # can place anything in the value place (even another dictionary)
    # dictionarys are wrapped around { }
    
# accessing values in dictionary
    # to get the value associated with the key
print(alien_0['color'])
new_points = alien_0['points']
alien_color = alien_0['color']
print(f"You just scored {new_points} points on the {alien_color} alien!")

# adding new key value pairs 
    # give the name of the dictionary followed by the new key in the square bracket, along with the new value
    # adding aliens x and y coordiantes, left side of screen, 25 pix down from the top
    # screen coordinates ususally start at the upper left corner of the screen, so x = 0, y = 25
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary 
    # start with empty curly braces, then add keys and values as needed 
alien_1 = {}
alien_1['color'] = "blue"
alien_1['points'] = 10
print(alien_1)
    # ususally use empty dictionaries to store large quantities of key value pairs 
    
# modifying values in a dictionary
    # give the name of the dic with the key in the square brackets and then the new value you want assoc for that key
    # for example changing alien color 
alien_1_color = alien_1['color']
print(f"Look a {alien_1_color} alien!")

alien_1['color'] = 'orange'
print(f"Look a {alien_1['color']} alien!")

    # now tracking an alien that can move at different speeds 
    # we will store the position of the alien moving 
print(f"Original position: {alien_0['x_position']}")
# move the alien to the right 
# determine how far to move the alien based on its current speed
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be the fast alien 
    x_increment = 3

# the new position is the old position plus the increment 
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


# removing key value pairs 
    # use the `del` statement to completly remove the key value pair, 
    # all del needs is the name of the dic, and the key to remove 
del alien_0['points']
print(alien_0)


# dictionarys of similar objects 
    # a simple poll of peeps fav langnueages 
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust',
    'phil': 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# using get() to access values 
    # lets see what happens if you ask for the point value that doesnt have a point value 
alien_0 = {'color': 'green', 'speed': 'slow'}
    # print(alien_0['points'])
    # this would recall in an error
    # for dictionaries, you can use the get method to set a default value that will be returned if the key doesnt exist
    # get() requires a key as the first arg, second (optional) value can be the value to be returned if nothing
point_value = alien_0.get('points', 'no point value assigned.')
print(point_value)
    # use get to not throw an error in code, and still get result of what youre looking for 
