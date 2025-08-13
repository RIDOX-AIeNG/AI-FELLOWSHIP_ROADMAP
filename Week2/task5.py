# Task1 Create and display
favorite_food1 = input("enter favorite dish: ")
favorite_food2 = input("enter favorite dish: ")
favorite_food3 = input("enter favorite dish: ")
dishes = []
dishes.append(favorite_food1)
dishes.append(favorite_food2)
dishes.append(favorite_food3)
print(tuple(dishes))
print("\n".join(dishes))

#Task 2 Tuple and INput
best_friend_name1 = input("Enter the name of your bestfriend: ")
best_friend_name2 = input("Enter the name of your bestfriend: ")
best_friend_name3 = input("Enter the name of your bestfriend: ")
best_friend_name4 = input("Enter the name of your bestfriend: ")
best_friend_name5 = input("Enter the name of your bestfriend: ")
friends = (best_friend_name1, best_friend_name2, best_friend_name3, best_friend_name4, best_friend_name5)
print(friends)
reversed_friend_name = friends[::-1]
print(reversed_friend_name)

#Task 3 Tuple Operations
states =[]
State1 = input("Enter your state: ")
State2 = input("Enter your state: ")
State3 = input("Enter your state: ")
State4 = input("Enter your state: ")
State5 = input("Enter your state: ")
print(State1,State5)
print("lagos" in states) 
print("lagos" not in states)
states.append(State1)
states.append(State2)
states.append(State3)
states.append(State4)
states.append(State5)
print(len(states))

#Task4 Tuple Unpacking
user_details = []
user_name = input("Enter firstname: ")
user_age = input("Enter your Age: ")
user_favColour = input("Enter Favorite Colour: ")
User_Town = input("Enter your Home town: ")
user_details = (user_name,user_age,user_favColour,User_Town)
user_name,user_age,user_favColour,User_Town = user_details
print(f"first name: {user_name} \nAge: {user_age} \nFavorite colour: {user_favColour} \nTown: {User_Town}")

#Task5 Modify Tuple Indirectly
shopping_list = []
item1 = input("Enter item; ")
item2 = input("Enter item; ")
item3 = input("enter item; ")
shopping_list = (item1,item2,item3)
updated = tuple(shopping_list)
ushop = list(updated)
print("Enter two more items")
item4 = input("Enter item; ")
item5 = input("Enter item; ")
ushop.append(item4)
ushop.append(item5)
ushop = tuple(ushop)
print('|'.join(ushop))

#Task6 Attendance Tracker
day = ("monday", "tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
month = ("january","february","march","april","may","june","july","august","september","october","november","december")
student_name = input("enter your name: ")
gender = input("Enter your gender")
course_Track = input('enter your track: ')
month_number = int(input("Enter current month number(1-12): "))
day_number = int(input("Enter current day number(1-12): "))
at_day = day[day_number-1]
at_month = month[month_number-1]
print(f"Name\t|Gender\t|courseTrack\t|MonthNumber\t|DayNumber\n{student_name}\t|{gender}\t|{course_Track}\t|{at_month}\t|{at_day}")