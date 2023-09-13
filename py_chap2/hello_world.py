print("hello python world!")

# printing messages to the terminal requires indicating of the python interpreter. for example "python3 hello_world.py". 
message = "hello python pt.2!"
print(message)

#VARIABLES

    # variable naming should be descriptive and concise, varibales should be all lowercase (uppercase inciating other meanings later on in a different chapter)
    # varibables should also include underscores between words not dashes

    # traceback, term used when error handling, example provided 
message = "hello traceback"
    # print(mesage)
    # when python3 hello_world.py is run in the terminal, the message showing that the traceback recived the most recent call in line 13 before it reached 'mesage'


#STRINGS

    # a data type, series of characters such as "hello", anything inside quotes can be considered a string
    # can be used with single or double quotes
    # for example
message = 'A wise man once said, "life is a highway"!'
print(message)

    # changing case in a string with methods 
name = "tom jones"
print(name.title())
    # similar actions 
    # print(name.upper())
    # print(name.lower())
    
    # using varibles in strings 
first_name = "calico"
last_name = "critters"
full_name = f"{first_name} {last_name}"
print(full_name)
    # to put variables into a string, place an f before 
    # another example
print(f"Hello, {full_name.title()}!")
first_name = "Calico"
last_name = "Critters"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()} friends!"
print(message)

    # adding whitespace to strings with tabs or newlines
    # whitespace = any nonprinting characters (spaces,tabs,end-of-line symbols), also use whitespace to organize output so its easier for users to read 
    
    # adding a tab
print("\tI'm tabbed")
    # adding newline to a string
print("Languages: \nPython\nC\nJavaScript")
    # now adding tab and list togehter 
print("Languages: \n\tPython\n\tC\n\tJavaScript")
    # stripping whitespace at the back of a string
fav_language1 = " python "
print(fav_language1.rstrip())
    # stripping whitespace at the front of a string
fav_language2 = " python "
print(fav_language2.lstrip())
    # stripping all of the white space 
fav_language3 = " python "
print(fav_language3.strip())
    # removing prefixes, ex. a URL https://
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
    # 
    
    # avoiding syntax errors 
message = "One of Python's strengths is its diverse community."
print(message)
    # if you use single quotes('') with apostrohes('s) this can cause syntax errors




    
