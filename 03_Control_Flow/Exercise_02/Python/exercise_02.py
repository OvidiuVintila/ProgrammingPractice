# Make a list of five or more usernames called current_users.
# •	 Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
# •	 Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
# •	 Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted.

current_users = ["User1","User2","Admin","User3","User4"]
new_users = ["User6","User7","Admin","User8","User2"]
for new_user in new_users:
    if current_users.count(new_user) == 0:
        print(f"The {new_user} can be used!")
    else:
        print(f"The {new_user} is already taken and can't be used!")