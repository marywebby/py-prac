# passing an arbitrary number of arguements 
    # sometimes you wont know ahead of time how many args a funciton needs to accept 
    # fortunetly, python allows a func to collect an arbitary number of args from the calling statement 
    # for ex, a func that builds a pizza, needs to accept a number of toppings, but you dont know how many a person wants
    # toppings param will collect as many args as the calling line porvides 
def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
    # now we can replace the print call with a loop that runs thorugh the toppins 
def make_pizza(*toppings): 
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# mixing positional and arbitrary arguements
    # if you want a func to accept different kinds of arguements,the param that accepts an arbritrary
    # number of arguements must be placed in the function definition
    # python matches positional and keyword arguements frist, and then collects any remaining arguements in the final parameters
    # for ex, if the func needs to take in a size for the pizza, that parameter must come before he parameter *toppings:
def make_pizza(size, *toppings): 
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(topping)
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# using arbitrary keyword arguements 
    # sometimes you want to accept an arbitrary number of args, but you wont know ahread of time what kinda of info will be passed to the function
    # in this case, you can write funcs that accept any key value pairs 
def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know know a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'eistien',
                             location='princetion', 
                             field='physics')
print(user_profile)
    
