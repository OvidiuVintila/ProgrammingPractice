# Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.
# Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
# person’s name.
# Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”

friends = ["Joe Rob", "Joe Doe", "Joe Add"]
transportation = ["car", "train", "plain"]
trasport_like = ["like", "don't like"]
message = "Nice to meet You,"

print(friends[0])
print(friends[1])
print(friends[2])

print(f"{message} {friends[0]}!")
print(f"{message} {friends[1]}!")
print(f"{message} {friends[2]}!")

print(f"My name is {friends[0]}, and I {trasport_like[0]} travel by {transportation[1]}!")