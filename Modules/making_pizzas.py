from pizza import make_pizza as mp

# or
# import pizza as p
# p.make_pizza(16, 'pepperoni')

# or
# from pizza import *


mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")

# We can also get variables from the module
from pizza import pizza_ingriedients

print(pizza_ingriedients)

# To list all functions and variables in a module, use the dir() function
import pizza

print(dir(pizza))
