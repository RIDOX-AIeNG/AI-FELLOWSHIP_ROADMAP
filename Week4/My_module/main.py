import first

import second

# lets use the functions in the first.py file

print("=== Math Functions ===")
print("5 + 3=", first.add(5,3))
print("10 - 4 =", first.subtract(10,4))
print("6 * 7 =", first.multiply(6,7))
print("20 / 5 =", first.divide(20, 5))

#   Lets us the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reserve of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))

