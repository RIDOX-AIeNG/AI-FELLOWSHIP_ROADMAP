#DICTIONARY 
#Keys- are unique and used to store and retrieve values
#Values - can be any data type (string, integer, list, tuple, even another dictionary)

#Syntax
# dictionary_name = {key1: value1, key2: value2}

#Creating Dictionaries 
#1. Using curly braces 
student = {
    "name": "Ada",
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
squares = {x: x**3 for x in range(1,6)}
print(squares)

#With Condition
#Dictionary of even numbers and their cubes 
even_cube = {x: x**3 for x in range(1,10) if x % 2 == 0}
print(even_cube)

#Using String keys

names = ["Ada","John","Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

#From Existing Dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}
#Filter students who passed (score >= 50)
passed_students = {name: score for name, score in students.items() if score >= 50}

#Define a dictionary
student = {"name": "Ada", "age": 20, "course": "computer Science"}

# Using key
print(student["name"])

#Using get() method (avoids errror if key is missing )
print(student.get('age'))
print(student.get("grade", "Not Found"))

#Modifying Dictionaries
#Removing Items from dictionaries

#1. Using pop()
student.pop("grade")
#2. Using popitem() - removes last inserted key_value
student.popitem()
#3.Using del keyword
del student["course"]
#4. Using clear() - removes all items
student.clear()
print(student)

#Dictionary Methods
# 1. keys()
person = {"name": "Emeka", "age": 30}
print(person.keys()) 

#2. Values()
print(person.values())

#3. items()
print(person.items())

#4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)

#Nested Dictionaries

students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}
print(students["student1"]["student2"]) #Access and nested 

#Looping Through Dictionaries
#Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

#Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)
# Loop through key-value pairs 
for key, value in student.items():
    print(f"{key}: {value}")

# Storing a student's biodata
student = {
    "name": "chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}    

print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")