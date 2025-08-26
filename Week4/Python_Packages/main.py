# my_module/main.py

import first
import second

# lets use the functions in the first.py file

print("")
print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Lets us the functions in the secon
print("")
my_rhyme = """
Black, black, black,
The color of the night.
Stars come out,
And the moon shines bright. 

Black, black, black,
The color of a shoe. 
Paint it nice,
It looks brand new!

Black, black, black,
The color of a cat. 
Soft and quick,
What do you think of that?
"""

print("My name is Micheal Scoffield. My my code message is: ", second.reverse_string(my_rhyme))
print("The total number of characters in my message is: ", second.count_characters(my_rhyme))
print("The total number of words in my message is: ", second.count_words(my_rhyme))
print("The total number of sentences in my message is: ", second.count_sentences(my_rhyme))