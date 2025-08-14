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