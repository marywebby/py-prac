# using a flag 
    # we just saw that we could have a program run while a condition was true, what if many conditions were true? 
    # for ex, in a game, several differnt events can end the game. 
        # such as a player runs out of ships, their tme runs out, or the cities they were to protect are gone
    # trying to test all these conditions in one while statement could prove trickey
    # for a programt that should run only as long as many conditions are true, you can define one variable
    # that determines whtehr the program is active 
    # this is called a flag, and acts as a signal to the program
    # we can make it so the program will run whenever the flag is set to true
    # and if any event sets the flag to false the program will stop
    # this helps so our while statement will only need to check one condition, if the flag is true
prompt = "\ntell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# this is the flag, called whatever we want
active = True
while active:
    message = input(prompt)
    # add in line to make it so it doesnt print `quit`
    if message == 'quit':
        active = False
    else: 
        print(message)
               
        
# using break to exit a loop
    # break statement, exit a loop without running any remaining code in the while
    # for ex, entering in places they have visited, we can stop the while loop in this program by calling break
    # as soon as quit is entered
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(please enter 'quit' when you are finished.) "

while True: 
    city = input(prompt)
    
    if city == 'quit': 
        break
    else: 
        print(f"id love to go to {city.title()}!")
              

# using continue in a loop
    # using a continue statement will return to the beginning of the loop, based on the result of a contional test
    # for ex, consider a loop that counts form 1 to 10, but rints only the odd numbers in that range
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: 
        continue
    
    print(current_number)
    
     
# avoiding infinate loops 
    # for ex, 
x = 1 
while x<= 5: 
    print(x)
    x += 1
    # if you accidently omit the line x +=1, the loop will run forever. 
    # press CNTRL C to exit out of an infinate loop and terminate the terminal 
    
