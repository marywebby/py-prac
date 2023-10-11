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
    # simplest way to do this is to based on the order of the arguements provided
    # values matched up this way are called positional args
def describe_pet(animal_type, pet_name):
    """display information about a pet"""
    print(f"I have a {animal_type}!")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')


# multiple function calls
    # you can call a function as many times as needed
    # describing a second differe animal and pet name would do so as:
describe_pet('dog', 'millie')


# order matters in positional arguements 
describe_pet('harry', 'hamster')
    # this would return I have a harry! My harry's name is Hamster.
    
    
# keyword arguements 
    # is a name-value pair that you pass to a function 
    # you pass the value associated with the arguement directly into the function call, so no confusion 
describe_pet(animal_type='fish', pet_name='gerald')
    # the func hasnt changed, we are telling python explitectly here what arg matched. 
    # these args can be flip flopped too
describe_pet(pet_name='doris', animal_type='frog')


# default values 
    # when writing a func, you can describe a default value for each parameter
    # default if no value is provided in the funciton call 
def descirbe_pet_sec(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}!")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
descirbe_pet_sec(pet_name='willie')
    # notice how the order had to be specified, this is because python interprets this as a positional argumnet
    # so if the function is called with just a pet name, that arg will match up with the first parameter listed in funcs definition 
    # then all you need to do is provide the pet name 
    # and then to add the animal type, the default value will be ignored
descirbe_pet_sec(pet_name='darla', animal_type='cat')


# equvilant function calls 
    # you can have several equvilant ways to call a function
# dog names willie
descirbe_pet_sec('willie')
descirbe_pet_sec(pet_name='willie')
# hamster named harry
descirbe_pet_sec('harry', 'hamster')
descirbe_pet_sec(pet_name='harry', animal_type='hamster')
descirbe_pet_sec(animal_type='hamster', pet_name='harry')


# avoiding argument errors 
    # unmatched arguements occur when you provide fewer or more args than a function needs to do its work
    # say you call
    # describe_pet()
    # python recognises that info is missing and provides a traceback call 
    
