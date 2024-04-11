# Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches . Then make an empty list called finished_sandwiches . Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches . After all the sandwiches have been made, print a 
# message listing each sandwich that was made .

sandwich_orders = ["Bagel toast","Baked bean","Barros Jarpa","Beef on weck"]
finished_sandwiches = []

while sandwich_orders:
  sandwich_in_order = sandwich_orders.pop()
  print(f"I've made your {sandwich_in_order}")
  finished_sandwiches.append(sandwich_in_order)

print(f"The sandwiches made are:")
for sandwich in finished_sandwiches:
  print(f"{sandwich}")