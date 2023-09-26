# at the heart of evey conditional statement is an expression that can be evaluated as true or false
    # this is called a conditional test
    # if true, python executes the code, if false, python moves past and continues to follow the if statement

# checking for equality 
    # most conditonal tests compare the current value of a varibale to a specific value of interest. 
    # the simplest conditioanl test checks whether the value of a varibale is equal to the value of interest. 
car = 'bmw'
print(car == 'bmw')
    # the first line set the value of car to bmw, single equal sign
    # next line '==', checks whether to value of car is bmw. 
    # called a equality operator, will return true is the value on the left and right side of ther operator match. 
audi = 'audi'
print(audi == 'bmw')
    # a single equal sign is a statement
    # read the first sign as "set the value of audi equal to audi"
    # read the next line as "is the value of audi equal to audi? "
    

# ignoring case when checking for equality
    # testing for equality is case sensitive in Python. 
    # two values with different capitalization are not considered equal
car = 'Audi'
print(car == 'audi')
    # if case matters, this behavior is advantageous
car = 'Audi'
print(car.lower() == 'audi')
    # useful to ensure unique usernames, not just variations of other peoples usernames with capital letters
    
    
# checking for ineqaulity 
    # when you want to determine is two values are not equal, you will use the inequality operater (!=)
req_topping = 'mushrooms'

if req_topping != 'anchovies':
    print("hold the anchovies!")


# numerical comparisons
    # following code checks whether a person is 18 yrs old 
age = 18
print(age == 18)
    # you can also test to see if two numbers are not equal 
answer = 17
if answer != 42: 
    print("that is not the correct answer. Please try again!")
    
    # you can also include various mathematical comparisons in your conditional statement as well 
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


# checking multiple conditions 
    # you may want to check multiple conditions at the same time
    # for ex, sometimes you might need 2 conditions to be true to take action. 
    # other times, you might be satisfied with just one condition being true. 
    # keywords `and` and `or` help you with this 
    
# using `and` to check multiple conditions 
    # if both tests pass it will be true 
    # if one or both fail, then it will be false 
age_0 = 22 
age_1 = 18 
    # for true 
print(age_0 >= 21 and age_1 >= 21)
    # for false
age_1 = 22 
print(age_0 >= 21 and age_1 >= 21)


# using `or` to check multiple conditions
age_0 = 22 
age_1 = 18
    # for true 
print(age_0 >= 21 or age_1 >= 21)
    # for false 
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


# checking whether a value is not in a list
    # you can use the keyword `not` in this situation 
    # ex, consider a list of users who are banned from commenting on a forum. 
    # you can check whether a user is has been banned before allowing them to comment 
banned_user = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_user:
    print(f"{user.title()}, you can post a response if you wish")
    

# boolean expressions 
    # another name for a conditional test 
    # boolean is either true or false, just like the value of a conditonal statement after its been evaluated 
    # boolean values are often used to keep track of certain conditions
        # such as whether a game is running or whether a user can edit certain content on a website
game_active = True
can_edit = False

