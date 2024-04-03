# Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
# Use the list above but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.
# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

names = ["Joe Rob", "Joe Doe", "Joe Add"]
transportation = ["car", "train", "plain"]
trasport_like = ["like", "don't like"]
message = "Nice to meet You,"

print(names[0])
print(names[1])
print(names[2])

print(f"{message} {names[0]}!")
print(f"{message} {names[1]}!")
print(f"{message} {names[2]}!")

print(f"My name is {names[0]}, and I {trasport_like[0]} travel by {transportation[1]}!")