# tuples 
    # allow you to create a list of items that you cannot change 
    # python refers to varibales that cannot change as immutable, also known as a tuple
    
    # they look just like lists, except you can use paratheses to instead of square brackets 
    # once made, their elements can be accessed just like a list by the index


    # for example, we have a rectangle that cannot change shape.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

    # lets see what happens when we try to change the dimensions of the rectangle
# dimensions[0] = 250
    #   dimensions[0] = 250
#     ~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
    # benefical because the traceback will tell us the tuple error 
    
    # tuples are defined the the comma, if you want to have just one element you can do this (3,)
    # the parathesis just make it look nicer 
    
# looping through values in a tuple 
for dimension in dimensions:
    print(dimension)
    
# although you cant modify a tuple, you can assign a new value to a variable that represents a tuple
    # for ex, if we want to change the dimensions of the rectangle, we could redefine the entite tuple 
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)  
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)