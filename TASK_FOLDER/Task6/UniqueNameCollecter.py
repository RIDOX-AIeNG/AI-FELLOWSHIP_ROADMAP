#Task2
#Unique name collector- Attendees of a seminar
#Create an empty attendees set
# attendees = set()
# #add names to the set
# attendees.add("Rukhayah")
# attendees.add("A'ishah")
# attendees.add("Badrudeen")
# #print the attendees 
# print("Attendees:", attendees)

attendees = set()
#add names to the set
att1 = attendees.add(input("Enter your name: "))
atte = attendees.add(input("Enter your name: "))
att = attendees.add(input("Enter your name: "))
#print the attendees 
seminar_att = attendees
print("seminar attendees:", sorted(seminar_att, key= lambda x:x.lower()))