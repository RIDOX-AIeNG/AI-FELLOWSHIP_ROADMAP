name = input("Enter your name: ")
try:
    if name.isalpha(): and "name" != 0:
    print(name)

    else:
        print("enter your name")
except ValueError:
    print("input a name")
age = int(input("enter your age"))
try:
    if len(age) != 0:
        print(age)
    else:
        print("enter your age")
except ValueError:
    print('Enter a number')

track = input("Enter your track: ")
if len(track) != 0:
    print(track)
else:
    print('Enter your track')

phone_number = int(input("Enter your PhoneNumber: "))
try:
    if len(phone_number) != 0:
        print(phone_number)
    else:
        print("Enter valid number")
except ValueError:
    print("Enter valid number")

contact_info ={
    "name":name,
    "age": age,
    "track": track,
    "phone number": phone_number
}
contact_info.update()

# contact_info.save_partcipant()