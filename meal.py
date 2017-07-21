
from random import *


#Create the list of words you want to choose from.
drinks = ["Water" , "sprite" , "coke" , "fanta" , "sparkling_water"]
Food = ["rice" , "beans" , "Fish" , "Potato" "Chicken"]
dessert = ["cake" , "donut" , "rolls" , "cookies" "flan"]

#Generates a random integer.
a = randint(0, len(drinks)-1)
b = randint(0, len(Food)-1)
c = randint(0, len(dessert)-1)
print(drinks[a])
print(Food[b])
print(dessert[c])
