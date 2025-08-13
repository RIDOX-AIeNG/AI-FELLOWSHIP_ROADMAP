# #Tuples - A tuple is an ordered, immutable (unchangeable) collection of items in python
# # Creating Tuples

# #1. Using Parenthesis()
# #Example 1: tuple with multiple items
# fruits = ("apple", "banana", "cherry")
# print(fruits) #('apple', 'banana', 'cherry')

# #2.Without parenthesis (tuple packing)
# numbers = 1, 2, 3
# print(numbers) # (1, 2, 3)

# #3. Single-item tuple (musyt include a comma)
# single_item = ("apple", 12)
# print(single_item)  #('apple',)
# print(type(single_item)) # <class 'tuple'>

# fruits_list = ["apple", "banana", "cherry"]
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple) 

# # Characteristics opf a tuple - They are orderd, immutable, Allow duplicates, can contain mixed data types, can be nested.

# # 1.Ordered 
# colors = ("red", "green", "blue")
# print(colors[0])
# #Immutable
# colors[1] = "yellow" #TypeError

# 2.Allow duplicates 
numbers = (1, 2, 2, 3)
print(numbers)  # (1,2,2,3)

#3. Mixed Data Types
mixed = ("apple, 3, True, 5.6")
print(mixed) # ('apple', 3, True, 5.6)
print(type(mixed))

#4. Nested Tuples
nested = (("a", "b"), (1,2))
print(nested) #(('a', 'b'), (1,2))

#Tuples Operations
# Even though tuples are immutable, you can still perform several operations

# 1. Indexing 
fruits = ("apple", "banana", "cherry")
print(fruits[1]) # banana
print(fruits[-1]) # cherry

# 2. Slicing 

print(fruits[0:2])  # ('apple', 'banana')
print(fruits[::1])  # ('cherry', 'banana', 'apple')

#3. Concatenation
tuple1 = (1,2)
tuple2 = (3,4)
result = tuple1 + tuple2
print(result) # (1,2,3,4)

# 4. Repetition
nums = (1,2)
print(nums * 3) # (1,2,1,2,1,2)

#5. Membership
fruits = ('apple', "banana", "cherry")
print("banana" in fruits) #True
print("grape" not in fruits) #True

# 6. Iteration
for fruit in fruits:
    print(fruit)

#Unpacking Tuples 
person = ('John', 25, "Nigeria") 
name, age, country = person
print(name)
print(age)
print(country)

#Tuple Methods - Tuples have only two methods 
# dot count() and dot index()

numbers = (1,2,2,3,4)

print(numbers.count(2))  #2
print(numbers.index(3)) #3

#Converting between list and Tuples

#Tuples to list
t = (1,2,3)
lst = list(t)
lst.append(4)
print(lst) # [1,2,3,4]

#list back to tuple
t = tuple(lst)
print(t) # (1,2,3,4)

#Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums)) #4
print(max(nums))  #7
print(min(nums))  #1
print(sum(nums))  #15