# making numerical lists 
    # ex.) keeping track of positions of each character in a game, keeping track of high scores. 
    # in data visualizations youll almost always work with sets of numbers, such as tmeps, distances, pop size, or lat or long coordinates. 
    
# using the range() function
    # makes it easy to generate a series of numbers. for ex, you can use the range () function to print a series of numbers like this
for value in range(1, 5):
        print(value)
    # in this ex, range() prints onlu the bumbers 1 through 4. this is another result of the off by one behavior youl often see in programming
    # range() causes python to start counting at the number you give it, so 1, and then stop right before the other number, because it stops at the 
    # second number, it will never print it. 

    # so if you want to print 5, youll have to do this 
for value in range(1, 6): 
    print(value)
    
    # you can also just pass one arguement whilin range(), and this will provide you with 0 through the number before the number you give it 
for value in range(4): 
    print(value)
    
    
# using range() to make a list of numbers 
    # if you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. 
    # so, when you wrap list() around a call to the range() function, the output will be a list of numbers. 
numbers = list(range(6))
print(numbers)

    # can also use range() to tell py to skip numbers. if you pass in a 3rd arguement into range(), python uses that value as a step size
even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(3,12,2))
print(odd_numbers)

# making a list of squared numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
    # here we start with an empty list called squares (line 36)
    # from there we tell python to loop through each value from 1 to 10, using range() (line 37)
    # inside the loop, the current value is raised to the second power and assigned to the variable square (line 38)
    # each new value of square is then appended to the list squares. 
    # and then finally, when the loop is finished, the lsit of squares is pritned. 
    # to write it more cleanly
squares2 = []
for value in range(1,11):
    squares2.append(value**2)
print(squares2)


# simple statistics with a list of numbers 
    # few python functions for finding the min, max and sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# list comprehensions 
    # allows you to generate this same list in just one line of code. 
    # list comprehensions combines the `for` loop and the creation of the new elements into one line, and
    # automatically append each new element
    # most likely to be soon later 
squares = [value**2 for value in range(1,11)]
print(squares)
    # to do this, start with a descriptive name for the list
    # next, open a set of square brackets and define the expression for the value 

# practice
    # sum of a million 
million = range(1,10000000)
print(sum(million))

    # cubes
cubes = []
for value in range(1,21):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1,26)]
print(cubes)


    