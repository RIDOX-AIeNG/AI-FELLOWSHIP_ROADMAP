# main.py

# Import the whole package
from math_utils import *
from string_utils import *

print(add(5, 3))           # 8
print(subtract(10, 4))     # 6
print(capitalize_text("python"))  # Python

# OR import specific modules
from string_utils import reverse_text

print(reverse_text("hello"))  # olleh