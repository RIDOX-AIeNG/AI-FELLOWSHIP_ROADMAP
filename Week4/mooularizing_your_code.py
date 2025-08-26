#Different ways of importing modules

#import the whole module
import math

# Lets put it to use

print(math.sqrt(9))

# 1. Import as an alias
import math as m

#lets put it to use
print(m.sqrt(25))

#3. Import specific function or variables
from math import sqrt, pi

print(sqrt(36))
print(pi)