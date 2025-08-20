# #Conditional Statement
# #If Statement
# age = 20
# if age >= 18:
#     print("You are eligible to vote")

# #If - Else statement
# wallet = 400
# price = 500

# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")


# #if_elif_else
# #For multiple conditions
# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C") 

# #Nested If
# # Plcing an if inside another if

# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")    


# #Loops

# #1. for loop - for iterating over a squence (strings,list,tuple,dictionary)
# fruits = ['apple','banana','orange']
# for fruit in fruits:
#     print(f"Ilike {fruit}")

# coordinates = (0.34654, -0.48585, 0.57477)
# for point in coordinates:
#     print(f"Point: {point}")

# student = {"name": "Tunde", "age": 16, "grade": "A"}
# for key,value in student.items():
#     print(f"{key}: {value}")


# word = "PYTHON"
# for char in word:
#     print(char)

# #While Loop - Used to repeatedly execute a block of code as long as a given condition is true.
# #Using while loop
# count = 1
# while count <= 5:
#     print("number: ", count)
#     count += 1


# #Increment with while
# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1

# # Decrement with while

# timer = 10
# while timer > 0:
#     print("countdown:", timer )
#     timer -= 1

# #While with User Input
# # Keep asking until the user enters a correct password 

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted!")

# # While True loop - it is an infinite loop as it continues until you explicitly stop it.
# while True: 
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")


# #Loop Control Statements (Break, Continue and Pass)

# #1. Break - Stops loop immediately. Used if a condition is met and there is no need to continue looping
# for num in range(1,10):
#     if num == 5:
#         break
#     print(num)

# #2. Continue - Skips the current iteration and moves to the next one. Used if you want tto ignore some values but keep the loop running.
# for num in range (1,6):
#     if num ==3:
#         continue
#     print(num)

#3. Pass - Does nothing. It is used when you haven't written the code yet but want to keep the structure.
# for num in range(1,6):
#     if num == 3:
#         pass # do nothing for now
#     else:
#         print(num)

# while True:
#     print("\Menu:")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")

#     choice = input("choose an option: ")

#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice == "3":
#         print("Existing program...")
#         break
#     else:
#         print("Invalid choice. Try again.")
    

# Using while True for validation
# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print(f"Your age is {age}")
#         break
#     else:
#         print("invalid input. Please enter a number.")

# #Lets make a guess
# secret = "Pyhton"

# while True:
#     guess = input("Guess the secret word: ")
#     if guess.lower() == secret:
#         print("Correct! You have guessed the word right.")
#         break
#     else:
#         print("Wrong! Try again..")

#Do you remember this?
balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            print('withdrawal successful.')
            print(f'New balance is {balance}')
        else:
            print("Insufficient funds")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option try again.")