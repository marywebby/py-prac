# if statments
    # progamming involves examining a set of conditions and deciding which action to take based on those conditions
    # py `if` statement allows you to examine the current state of a program, and respond appopriatly to the state
    # once you grasp the concepts of conditional tests, then you can apply this concepts to lists 
    # then youll be able to write a for loop, handling some items in one way, and others in a different way

# simple example 
    # following ex shows how if tests let you respond to special situations correctly 
    # list of cars and you want to print out the name of each cars(proper names, so need .title().)
    # however, you need bmw to be printed in all uppercase
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())
    
