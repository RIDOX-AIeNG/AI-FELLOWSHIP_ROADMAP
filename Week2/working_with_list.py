empty_list = []
print(empty_list) # Output: []

#Method 2: Using the list() constructor 
empty_list2 = list()
print(empty_list2) #Output

#list of integers 
numbers = [1,2,3,4,5]
print(numbers) #output: [1,2,3,4,5]

# list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['Alice', 25, 5.8, True]

#Mixed data tyopes 
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list) #output ['Alice', 25, 5.8, True]

#From a string (each character becomes an element)
chars = list("hello")
print(chars) # Output: ['h', 'e', 'l','l','o']

#From a tuple
#my_tuple = (10,20,30) list_from_tuple = list(my_tuple) print(list_from_tuple) #Output:[10,20,30]
#From a range 
#numbers_range = list(range(5)) print(numbers-range) #Output: [0,1,2,3,4]

#Creating a list using list comprehension. List comprehensions are concise way to create lists using a loop in one line

# squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares) #Output: [0,1,4,9,16]

#Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens) #output: [0,2,4,6,8,10]

#Creating a nested list. A list can be contained in another list. It is useful in matrices and grouped data
#Matrix-like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix) #Output: [[1,2], [3,4], [5,6]]

#Accessing elements in a nested list
print(matrix[0])   #Output: [1,2]
print(matrix[0][1]) # Output: 2

#Characteristics of a list
# 1. Ordered Collection

fruits = ["mango", "orange", "mango"]
print(fruits)  #['mango', 'orange', 'banana']
print(fruits[0]) #output: mango
print(fruits[1]) #output: orange

# 2. Allow duplicates
#it can store the same value multiple times
items = ["rice", "beans", "yam", "rice"]
print(items) #Output; ['rice', 'beans', 'yam', 'rice']

#3. Mutable (can be changed)
numbers = [1,2,3]
numbers[1]= 20
print(numbers) #[1,20,3]

#4. Can contain different data types 
#A list can hold integers,strings, floats , booleans, and even other lists
mixed = [10, 'nigeria', 3.14, True]
print(mixed) #[10, 'nigeria', 3.14, True]

#5. Can be nested 

nested_list = [[1, 2], ["a"], "b"]
print(nested_list)
print(nested_list[0][1])
      
#Dynamic Size - You dont need to declare the size of a list forhand
name = ["Ada"]
name.append("Bola")
name.append("chidi")
print(name)