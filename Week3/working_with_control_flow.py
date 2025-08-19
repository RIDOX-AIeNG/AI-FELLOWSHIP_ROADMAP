#Conditional Statement
#If Statement
age = 20
if age >= 18:
    print("You are eligible to vote")

#If - Else statement
wallet = 400
price = 500

if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")


#if_elif_else
#For multiple conditions
score = 85
if score >= 70:
    print("Grade A")
elif SCORE >= 50:
    print("Grade B")
else:
    print("Grade C") 

#Nested If
# Plcing an if inside another if

age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")    


#Loops

#1. for loop - for iterating over a squence (strings,list,tuple,dictionary)
fruits = ['apple','banana','orange']
for fruit in fruits:
    print(f"Ilike {fruit}")

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key,value in student.items():
    print(f"{key}: {value}")


word = "PYTHON"
for char in word:
    print(char)

#While Loop - Used to repeatedly execute a block of code as long as a given condition is true.
#Using while loop
count = 1
while count <= 5:
    print("number: ", count)
    count += 1


#Increment with while
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1

# Decrement with while

timer = 10
while timer > 0:
    print("countdown:", timer )
    timer -= 1

#While with User Input
# Keep asking until the user enters a correct password 

password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access Granted!")