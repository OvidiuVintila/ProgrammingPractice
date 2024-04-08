# Make a list of five or more usernames, including the name 
# 'admin'. Imagine you are writing code that will print a greeting to each user 
# after they log in to a website. Loop through the list, and print a greeting to 
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.,

user_list = ["User1","User2","Admin","User3","User4"]
for user in user_list:
    if user == "Admin":
        print(f"Hello {user}, would you like to see the status report?")
    else:
        print(f"Hello {user},thank you for loggin in again! ")