#List operations in python
#1. Concatenation (+)
#join two lists into a new list
list1 = [1,2,3]
list2 = [4,5]
result = list1 + list2
print(result) # [1,2,3,4,5]

#Repetition (*) - Repeats elements in a list a ngiven number of times 
nums = [1,2]
repeated = nums *3 
print(repeated) # [1,2,1,2,1,2]

#3. Indexing - Access elememnts using their position(starting from 0).

fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  #apple
print(fruits[-1])  #cherry  (negative index starts from th end)

#4. Slicing  - Extract a portion of the list

numbers = [0,1,2,3,4,5]
print(numbers[1:4]) #[1,2,3]
print(numbers[:3]) #[0,1,2]
print(numbers[3:]) # [3,4,5]
print(numbers[::2]) # [0,2,4] (step of 2)

#Membership (in/ not in) - checks if an elemenmt exists in a list

colors = ["red", "green", "blue"]
print("green" in colors ) #True
print("yellow" not in colors) #True

#6. Lenght (len()) - counts the number of elemengts in a list
items = ["pen", "book", "laptop"]
print(len(items)) #3

#7. Min and Max (min()/ max()) - Returns the smallesst or largest element
nums = [5,2,9,1]
print(min(nums))
print(max(nums))

#8 Sum (sum()) adds all numerical elements in a list

numbers = [1, 2, 3, 4]
print(sum(numbers))

#9. List Comprehension 
squares = [x**2 for x in range(5)]
print(squares)

#10. Copying a list - Creates a duplicate list 

a = [1, 2, 3]
b = a.copy()  # or b = list(a)
print(b) # [1,2,3]
