# learn how to accept user input so your program can then work with it 
    # to do this, we will use the input() function 
    # we will use pythons  `while` loop to keep the program running as long as certian condition remain true



# the input() function 
    # this will pause your program and wait for the user to enter some text, 
    # once text is recieved, it assigns that input to a varibale to make it convenient for us to work with
message = input("Tell me something, and i will repeat it back to you: ")
print(message)
    # the input will take one arguement, the prompt
    # the program waits until the user types and enters something, and then contiues the program



# writing clear prompts
    # everytime you use input() function, you should include a clear easy to follow prompt. 
# name = input("Hello, please enter your name: ")
# print(f"Hello! {name}!")



# writing more than one line 
    # for ex, you might want to tell the user why youre asking for certain input.
    # you can assign your prompt to a varibale and pass that variable to the input() funtion
    # this allows you to build your prompt over several lines, then write a clean input() statement
prompt = "If you share your name, we can personilze the messages you see."
prompt += "\nWhat is your first name: "

name = input(prompt)
print(f"Hello! {name}!")



# using int() to accept numerical input 
age = input("how old are you?: ")
age = int(age)
    # if you are taking in an integar for a numerical funtion, such as age >= 18, the input()
    # funciton would result in an error because it it reading the input as a string not a number
    # you have to then convert the input into a integar
print(age >= 18)
    # lets see it in full action 
height = input("how tall are you in inces?: ")
height = int(height)

if height >= 48:
    print("\nCongrats you are tall enought to ride!")
else:
    print("\nSorry, no ride for you :()")
    


# the modulo operator 
    # useful tool for working with numberical information is the mod operator %
    # this will devide one number by another number and return the remainder
print(4 % 3) 
    # this would return 1 
    # doesnt tell you how many times the number can be divided by just the number thats left over once done
number = input("Enter a number, and ill tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nthe number {number} is even")
else: 
    print(f"\nthe number {number} is odd")
    
