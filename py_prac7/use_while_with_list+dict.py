# using a while loop with lists and dictionaries 
    # taking in user information and storing it in lists and dictionaries while using a while loop 
    # a for loop is effective for looping through a list, but you shouldnt modify a list inside a for loop
    # because python will have toruble keeping track of the items in the list
    # to modify a list as you work through it, you should use a while loop
    
# moving items from one list to another 
    # consider newly register but not verified users on a website
    # after we verify these users, how can we move them to a seperate list of confirmed users?
    # one way would be to use a while loop to pull users from the list of not confirmed users as we verify them
    # and then add them to a seperate list of confirmed users 
# start with users that need to be verified
# and an empty list the hold confirmed users 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users
# move each verified user into the list of confirmed users 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# display all confirmed users
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    
    
    
# removing all instances of specific values from a list
    # in chap 3, we used remove() to remove specific value form a list
    # the remove function worked because there was only one specific value in the list we wanted to remove
    # what if you want to remove all instances in a list?
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)



# filling a directory with user input
    # you can prompt for as much input as you need in each pass through a while loop 
    # you can make a polling program in which each pass through the loop prompts for the part. name and repsonse
    # we will store the data in a dictionary
    # because we want to connect the name with the response 
responses = {}
# set a flag to indicate that polling is active 
polling_active = True
while polling_active:
    # prompt for the persons name and reponse
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like the climb someday? ")
    
    # store the response in the dict
    responses[name] = response
    
    # find out if anyone else is going to take the poll
    repeat = input("would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# polling is complete, show the results
print("\n------poll results------")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")