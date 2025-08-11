#Upper
name = "Ada Balogun"
print(name.upper()) # output: Ada Balogun 

#title() converts all characters in the string to lowercase
sentence = "python is amazing"
print(sentence.title()) #output: Python is Amazing

#Strip
#Removes whitespace (or specified characters) from both ends of the string.
text = "   Abuja   "
print(text.strip())   #output Abuja

#replace
#replaces occurrences of a substring with another substring
message = "I love Java"
print(message.replace("Java", "Python")) # Output: I love Python.

#swapcase
#Switches lowercase to uppercase and viceversa.

text = "Hello ABEOKUTA"
print(text.swapcase()) #output: hELLO abeokuta

#lstrip() Removes whitespace (or specidfied characters) from the left side only.

text = "   Nigeria"
print(text.lstrip()) #Output: Nigeria

#rstrip()  Removes whitespaces (or specified characters) from the right side only
text = "Nigeria   "
print(text.rstrip()) #Output: Nigeria

#split() splits a string into a list using a separator (default is space)
fruits = "mango orange banana"
print(fruits.split()) # Output: ['mango', 'orange', 'banana']

#rslpit() splits a string into a list from the right side.
text = "one,two,three,four"
print(text.rsplit(",", 2)) #output: ['one,two', 'three', 'four']

#slpitlines()
# splits a string nto list at each newline (\n)
lines = "line 1\nline 2\nline 3"
print(lines.splitlines())  #Output: ['line 1', 'line 2', 'line 3']

#join()
#joins a list of strings into one string with a specified separator

words = ["I", "love", "Python"]
print(" ".join(words)) # Output: I love python

#center()
#centres the string within a specified width, padding with spaces or characters

text = "python"
print(text.center(21, "-"))  # Output: -----Python------

#ljust()
#left-aligns the string within a specified width, padding with spaces or characters.
text = "python"
print(text.ljust(10, "*")) #output: Python

#zfill
# Pads a numeric string on the left with zeross until it reahes a given length

num = "42"
print(num.zfill(5)) #output 00042

#isalpha() checks if the string contains only letters.

print("Lagos".isalpha()) #True
print("Lagods123".isalpha)
      
