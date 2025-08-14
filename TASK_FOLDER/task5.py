# Task1 Create and display
# Collecting user input
favorite_food1 = input("enter favorite dish: ")
favorite_food2 = input("enter favorite dish: ")
favorite_food3 = input("enter favorite dish: ")
dishes = []
#storing the input in a tuple "dishes"
dishes.append(favorite_food1)
dishes.append(favorite_food2)
dishes.append(favorite_food3)
#printing the tuple in a single line mode and separated by commas
print(tuple(dishes))
print("\n".join(dishes))

#Task 2 Tuple and Input
#Collecting users input
best_friend_name1 = input("Enter the name of your bestfriend: ")
best_friend_name2 = input("Enter the name of your bestfriend: ")
best_friend_name3 = input("Enter the name of your bestfriend: ")
best_friend_name4 = input("Enter the name of your bestfriend: ")
best_friend_name5 = input("Enter the name of your bestfriend: ")
#Storing users input in a tuple
friends = (best_friend_name1, best_friend_name2, best_friend_name3, best_friend_name4, best_friend_name5)
#printing tuple
print(friends)
#printing the result in reversed mode
reversed_friend_name = friends[::-1]
print(reversed_friend_name)

#Task 3 Tuple Operations
# Creating a tuple consisting of 5 (states)
states =[]
State1 = input("Enter your state: ")
State2 = input("Enter your state: ")
State3 = input("Enter your state: ")
State4 = input("Enter your state: ")
State5 = input("Enter your state: ")
#printing the first and last states
print(State1,State5)
#checking if lagos is included in the states or not
print("lagos" in states) 
print("lagos" not in states)
#compiling the states in a tuple "states"
states.append(State1)
states.append(State2)
states.append(State3)
states.append(State4)
states.append(State5)
# Printing the number of states in the tuple
print(len(states))

#Task4 Tuple Unpacking
#Collecting user details
user_details = []
user_name = input("Enter firstname: ")
user_age = input("Enter your Age: ")
user_favColour = input("Enter Favorite Colour: ")
User_Town = input("Enter your Home town: ")
#Storing the details in atuple and unpacking into variables
user_details = (user_name,user_age,user_favColour,User_Town)
user_name,user_age,user_favColour,User_Town = user_details
#printing the result usinfg escape sequence so as to align the informations neatly.
print(f"first name: {user_name} \nAge: {user_age} \nFavorite colour: {user_favColour} \nTown: {User_Town}")

#Task5 Modify Tuple Indirectly
# Collecting users input for a shopping list
shopping_list = []
item1 = input("Enter item; ")
item2 = input("Enter item; ")
item3 = input("enter item; ")
shopping_list = (item1,item2,item3)
#storing in a tuple 
updated = tuple(shopping_list)
#converting to a list
ushop = list(updated)
#asking the user to enter two more items
print("Enter two more items")
item4 = input("Enter item; ")
item5 = input("Enter item; ")
ushop.append(item4)
ushop.append(item5)
#Converting the list to a tupple
ushop = tuple(ushop)
#printing the updated list using join and separating by "|"
print('|'.join(ushop))

#Task6 Attendance Tracker
#Creating an attendance tracker
#storing the days and month in a tuple.
day = ("monday", "tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
month = ("january","february","march","april","may","june","july","august","september","october","november","december")
#Collecting student details
student_name = input("enter your name: ")
gender = input("Enter your gender")
course_Track = input('enter your track: ')
#Creating an input sysytem for the month and day student was around 
month_number = int(input("Enter current month number(1-12): "))
day_number = int(input("Enter current day number(1-12): "))
at_day = day[day_number-1]
at_month = month[month_number-1]
print(f"Name\t|Gender\t|courseTrack\t|MonthNumber\t|DayNumber\n{student_name}\t|{gender}\t|{course_Track}\t|{at_month}\t|{at_day}")