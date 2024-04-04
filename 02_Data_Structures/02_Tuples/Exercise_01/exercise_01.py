# A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the 
# change.
# •	 The restaurant changes its menu, replacing two of the items with different 
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

food_recipes = ("Lemon Pasta Pronto","Salad-Stuffed Peppers","Sheet Pan London","Salmon Cakes","Beans Parmesan")
print(food_recipes)
for recipe in food_recipes:
    print(recipe)
    
#food_recipes[1] = "Sheet Pan London Broil"
#print(food_recipes[1]) #error TypeError: 'tuple' object does not support item assignment is shown 

food_recipes = ("Baked Chicken Tacos","Sheet Pan London","Salmon Cakes","Beans Parmesan","Creamy Chicken Soup")
for recipe in food_recipes:
    print(recipe)

