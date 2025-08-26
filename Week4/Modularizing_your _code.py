# #Modularity
# #Functions
# #Built-in Functions

# #see Examples of use here

# # range()
# for i in range(3):
#     print(i) # 0,1,2

# #zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# #map()
# nums = [1,2,3,4]
# squared = list(map(lambda x: x%2 == 0, nums))
# print(squared)  # [False,True,False,True]

# nums = [1,2,3,4]
# squared = list(map(lambda x: x**2 , nums))
# print(squared)  # [1,4,9,16]

# #Filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums) # [2,4]

# #Student performance feedback

# #step1 : Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter secomnd student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter secomnd student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# #Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# #Step 3: Display data
# print("\nStudent Data")
# for index, (n,s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("\nTotal Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# #Step 5: Ramnking (using sorted and zip)
# ranked = sorted(zip(scores, names ), reverse = True)
# print("\nRanking: ")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# #Step 6: Check data types 
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# #Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n,upper(), names))
# print("Uppercase Names:", upper_names)

# #Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)

#USER-DEFINED FUNCTION

#Defining a function
# def greet():
#     print("Hello, Welcome to AI Fellowship!")

# # When you want to use a function, this is how to call it.
# # And you vcan call it as many times as possible.
# greet()
# greet()

# #Function Arguments and Parenthesis
# def greet(name):
#     print('Hello', name, "Welcome to python Learning!")

# # Calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

# #When to use return, print() and yield keywords inside a function.
# #Print
# def greet(name):
#     print("Hello", name)

# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)

# #Return
# def add(a,b):
#     return a + b

# #Functional call

# result = add(4,6)
# print("The sum is:", result)

# #Note the output and compare it with that of print()

# # Yield

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i  # pause and return i
#         i += 1

# # Using the genrator
# for number in count_up_to(5):
#     print(number)

#Note the output:

#1. Positional Arguments
#The oprder of the arguments matters

# def introduce(name, track):
#     print("My name is ", name)
#     print("I am learning", track, ".")

# # function call
# introduce("Ngozi", "AI Engineering") #correct order

# # Change the arrangement and watch the output

# introduce("AI Engineering", "Ngozi") #Incorrect order, this will throw a semantic error

#2. Keyword Arguments

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call 
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangement and watch the output

introduce(track = "AI Engineering", name= "Ngozi")

#3. Default Arguments
def introduce(name, track = "AI Engineering"):
     print("My name is", name)
     print("I am learning", track,".")

#function call
#without specoifying the default argument, watch the output
introduce("Paul")

# Specify the default argument and watch the output

introduce("Tunji Paul", track = "AI Development")


#4. Varying Length Arguments
# a. Non-keyword(tuple)

def add_numbers(*args):
     total = 0
     for num in args:
          total += num
     print("Sum:", total)

# function call
# Take note of the output
add_numbers(2,4,6)
add_numbers(10,20,30,40,50)

#b. Keyword argument(dictionary)

def student_details(**kwargs):
     for key, value in kwargs.items():
          print(key, ":", value)

# functional call - Take note of the ooutput
student_details(name='peter', track = "AI Engineering", interest="Block Chain")

#Define student profile function
# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together

def participant_profile(name, age, track= "AI Development", *skills, **extra_info):
     """
     Generate a profile for a bootcamp participant using different types of arguments.
     """
     profile  = f"\n--- Bootcamp Participant Profile ---\n"
     profile += f"Name: {name}\n"
     profile += f"Age: {age}\n"
     profile += f"Track: {track}\n"

     #skills (from *args)
     if skills:
          profile += "Skills: " + ", ".join(skills) + "\n"
     else:
          profile += "Skills: Not yet specified\n"

    #Extra info (from **kwargs)
     if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
             profile += f" - {key.capitalize()}: {value}\n"
     return profile  

#Example 1: Using only   