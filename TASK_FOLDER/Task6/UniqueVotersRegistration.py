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