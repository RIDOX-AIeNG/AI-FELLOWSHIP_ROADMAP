#DICTIONARY 
#Keys- are unique and used to store and retrieve values
#Values - can be any data type (string, integer, list, tuple, even another dictionary)

#Syntax
# dictionary_name = {key1: value1, key2: value2}

#Creating Dictionaries 
#1. Using curly braces 
student = {
    "name": "Ada"
    "age": 20,
    "course": "computer Science"
}
print(student)

#2. Using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info)

#3. Empty dictionary
empty_dict = {}
print(empty_dict)

#4. Dictionary Comprehension
#Syntax:
