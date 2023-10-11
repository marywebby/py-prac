# passing a list
    # when you pass a list into a function, you the func gets direct access to that list
def greet_users(names): 
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# modifying a list in a function 
    # when you pass a list to a function, the function can modify the list. 
    # any changes made to the list inside the body of the fucntion are permanent
# start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendent', 'dodechahedron']
completed_models = []

# simulate printing each desgin, until none are left 
# move each design to completed_models after printing
while unprinted_designs: 
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    
# display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
# restructering it 
def print_models(unprinted_models, completed_models):
    """
    simulate printing each design, until none are left 
    move each design to completed_models after pritning
    """
    while unprinted_designs: 
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendent', 'dodechahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# preventing a func from modifying a list 
    # in the previous example, the func took all the elements out of unprinted models, but say we can to keep the orginal list?
    # this is where we make a copy, and any changes will be made to the copy
# function_name(list_name[:])
    # slice notation [:] makes a copy of the list to send tot he function. 
    
print_models(unprinted_designs[:], completed_models) 