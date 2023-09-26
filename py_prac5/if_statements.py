# if statements 
    # once you understand conditonal statements, you can begin to write if statements 
    # different kinds of if statements exist
 
    
# simple if statements
    # one test and one action 
    # if (conditonal test): do something 
    # if the condtional is true, python will excecute, if false, python will not
    # lets test if someone can vote 
age = 19
if age > 18:
    print("you are old enough to vote!")
    # indentation plays the same role here as it did for `for loops`
    # all indented lines after an `if` statement will be executed if the test passes, and will be ignored if not
    # you can add more to the indented block of code as well
    print("have you registered to vote yet?")


# if/else statements 
    # often you want to take one action when a conditonal passes, and another if it does not 
    # pythons `if/else` syntax makes this possible
else: 
    print("sorry, you are too young to vote")
    print("please register to vote when you turn 18")


# if/elif/else chain 
    # python executes only one block in this style of chain it runs each conditonal test in order, until one passes
    # when a test passes, that code is executed, and the following code will be skipped
    # many real world situations involve more than 2 possible conditions. 
    # for example
        # addmission for anyone under age 4 is free
        # admission for anyone between the ages of 4 and 18 is $25
        # admission for anyone 18 or older is $40
age = 12 
if age < 4:
    print("addmission is $0")
elif age < 18:
    print("addmission is $25")
else: 
    print("addmission is $40")  
    # instead of adding `print("addmission is $0")`, we can add that in later  
age = 23 
if age < 4:
    price = 0
elif age < 18:
    price = 25
else: 
    price = 40  
print(f"Your admission cost is ${price}.")

# using multiple elif blocks 
age = 67
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: 
    price = 20
print(f"Your admission cost is ${price}.")


# omitting the else block 
    # python does not require an else block at the end of an elif chain
    # sometimes the block is useful, other times, 
    # its clearer to use an additional elif statement that catches the specific condition of interest
    # else block is just a catch all, if you want certain answers, do not add and else 
    
# testing multiple conditions 
    # if/elif/else is only used if you need one conditonal to pass. 
    # once python finds one test to pass, it skips the rest. 
    # if you want to check all conditions of interest, then you should use a series of if statements with no elif or else
    # this condition makes sense if you want to act on every condition that is true
    # for ex, the pizzeria, if someone requests a two topping pizza, you need to be sure to include both 
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms!")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni!")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese!")
    
print("\nFinished making your pizza!")
    # this code would not work if we added if elif else block because it would stop running after the first if



# using if statements with lists
    # you can watch for spcial vlues that need to be treated different than other values in the list
    # also efficently manage changing conditons, such as avaliability of certin items in a resturant 
    
# checking for special items in a list 
    # you can now watch for specail items inside of a list 
    # for the pizzeria example, the pizzeria displays a message whenever a topping is added to your pizza, ad its being made
    # the code for this action can be efficently written by making a list of toppings the customer has requested
    # and then using a loop to annouce each topping as its added to the pizza 
requested_toppings = ['mushrooms', 'green pepper', 'extra cheese', 'pepperoni']
print("\nstarting your pizza!")
for requested_topping in requested_toppings:
    print(f"\nAdding {requested_topping}.")
print("\nFinsihed making your pizza!")

# checking a list isnt empty
    # soon we will let users add items into the list, however if a list is empty, its useful to check before it runs 
    # for pizza, if list is empty, tell user to add toppings 
requested_toppings = []
if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}.")
    print("\nFinsihed making your pizza!")
else: 
    print("Are you sure you just want a plain pizza?")
    
    
# using multiple lists
    # if they want to add something else to the lists, you can use lists and if statements to make sure your input makes sende before you act on it 
    # lets watch out for unusual toppings requests before we build a pizza. 
    # we have two lists, avaliable toppings and requested toppings, in which requested will be checked against avaliable
avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print(f"Adding {requested_topping} to pizza!")
    else:
        print(f"Sorry, we dont have {requested_topping}.")
print("Finished making pizza")