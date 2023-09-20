# looping through an entire list 
    # ex. moving every element on the screen at the same itme by the same amount. or perform the same action on every number. 
    # use python `for` loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    # first we define the list `magicians` then we define the loop: in which we tell python to pull a element from the string, and associate with the varibale magician.
    # magician on line 5, can be any value, but for convention, its best for the value to be a singular version of the plural

# spicing it up
    # adding in other tasks for `print(magician)` 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"{magician.title()}, you should do it again!")
    # you can add as many indented lines under the `for` loop, python will read as an action from line 13. 
    # considered "inside the loop"
    print(f"I cant wait to see your next trick {magician.title()}.\n")

# when a `for` is finished 
    # the for loop will stop excecuting when the next line is not indented 
print("Thank you for the show magicians!")
    
# summary,
    # could be used for listing out characters of a game and then at the end you add a start button to the function

# avoiding indentation errors 
    # python uses whites space to show where code is being excecuted in different functions. 
    # many common errors can be indenting when you do not need to be indenting, and forgetting to indent. 
    # forgetting to add inent additional lines 
    # indenting unnecessarily
    # indenting unnecessarily after the loop 
    # forgetting the colon 

