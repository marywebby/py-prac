# return values 
    # a func doesnt always have to display its output directly
    # it can process some data and then return a value or set of values 
    # the value the func returns is called a return value 
    # the return statment takes a vaue from inside a function and sends it back
    # these allows you to move much of your programs grunt work into functions, which can simplify your body


# returning a simple value 
def get_formatted_name(first_name, last_name): 
    """return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# making an arguement optional 
    # this helps with people using the funciton can choose to provide estra infomation only if they want to
    # say we want to expand get formatted name
def get_formatted_name_two(first_name, middle_name, last_name): 
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician_two = get_formatted_name_two('john', 'lee', 'hooker')
print(musician_two)

    # but middle names arent always needed 
    # we can change this by adding
def get_formatted_name_three(first_name, last_name, middle_name=''): 
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"  
    return full_name.title()

musician_three = get_formatted_name_three('hilary', 'duff')
print(musician_three)

musician_four = get_formatted_name_three('tom', 'jones', 'lee')
print(musician_four)
    
    
# returning a dictionary 
    # the following func takes in parts of a name and returns a dictuonary representing a person
def build_person(first_name, last_name):
    """return a dictionary of info about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendricks')
print(musician)
    # you can also add in other information 
def build_person(first_name, last_name, age=None):
    """return a dictionary of info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendricks', age=27)
print(musician)


# using a func with a while loop
def build_person(first_name, last_name):
    """return a dictionary of info about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

# this is an infinate loop
# while True: 
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Lat name: ")
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"hello, {formatted_name}!")
    
    # we havent defined a way to quit
while True: 
    print("\nPlease tell me your name:")
    print("(enter q to quit at any time)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Lat name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"hello, {formatted_name}!")