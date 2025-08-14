#Task1 - Fruit Collector 
#Asking for the user information - 5 Favorite Fruits
fruits = {}
fav1 = input("Enter favorite fruit: ")
fav2 = input("Enter favorite fruit: ")
fav3 = input("Enter favorite fruit: ")
fav4 = input("Enter favorite fruit: ")
fav5 = input("Enter favorite fruit: ")
fruits = {fav1,fav2,fav3,fav4,fav5}
print(fruits)

#Task2
#Unique name collector- Attendees of a seminar
#Create an empty attendees set
attendees = set()
#add names to the set
attendees.add("Rukhayah")
attendees.add("A'ishah")
attendees.add("Badrudeen")
#print the attendees 
print("Attendees:", attendees)

#Task3
#Simulate a football match ticket system
#create at seat number from number 1  to 50
seat_range = range(1,51)
#put it in a set
seat_number = set(seat_range)
#input a seat number 
book_a_seat = int(input("Enter seat number: "))
#create a system that recognizes and remmoves a formerly inputed seat number
seat_number.remove(book_a_seat)
#print the remaining seat number
print(seat_number)

#Task 4
##Creating a unique voters Registration System
#create an empty set - registered
registered = set()
#collect users name
Voters_name = input("Enter your name: ")
#append it to the empty set
registered.add(Voters_name)
#collect another users name
Voters_name1 = input("Enter your name: ")
#append it to the empty set
registered.add(Voters_name1)
#Create at system that checks for duplicates and indicates.
if Voters_name1 in registered:
   print(f"{Voters_name1} has already being registered")
else:print(f"{Voters_name1} has been succesfully registered ") 
#print the number of registered voters 
print(len(registered))