# functions 
    # blocks of code designed to do one specific job
    # "call" on functions when wanting to perfrom 


# defining a func 
def greet_user():
    """display a simple greeting."""
    print("hello!")

greet_user()
    # indented lines below def are called the body 
    # line 7 is called a docstring, it describes what the func does
    
    
# passing information into a func
    # passing username into the functions definition will allow you to use this info in the body
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('mary')


# args and parameters 
    # the varibale user name in the def of greet_user(username) is an argument 
    # arg is a piece of info thats passed from a function call to a funciton 
    
    
# passing arguements 
    # pass args into a fucntion number of ways 
        # positional args, which need to be in the same order the parameters were written 
        # keywords args, where each arg consists of a varibale name and a value
        

# positional arguements 
    # when you call a function, py must match each arg in the func with a parameter in the func definition
