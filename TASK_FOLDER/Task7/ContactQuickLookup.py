#Contact Quick LookUp
#Create two tuples, store names and numbers in each tuple
#Create a function to collect a users name such that their number is displayed
#Use Zip() and dict() to combine tuples and . get for retreival
names = ("Osho", "Ayoola", "ola")
phone_numbers = ("09789657456", "08234567865", "09123456789")
contact_info = dict(zip(names, phone_numbers))
print(contact_info)
name = input("Enter a name to search for their phone number: ")
print(contact_info.get(name, "Name not found"))