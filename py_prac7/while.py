# while loops
    # runs while a certian condition is true
    # you can use a while loop to count up through a series of numbers. for ex, the following loop counts to 1 to 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 
    # `current_number += 1` is shorthand for current_number = current_number + 1
    

    
# letting the number choose when to quit
    # we can make this program run as long as the user wants by putting most of the program inside a while loop
    # we will define a `quit value` and then keep the program running as long as the user has not entered the quit value
prompt = "\ntell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    # add in line to make it so it doesnt print `quit`
    if message != 'quit':
        print(message)
        
        
        
# using a flag
    # 