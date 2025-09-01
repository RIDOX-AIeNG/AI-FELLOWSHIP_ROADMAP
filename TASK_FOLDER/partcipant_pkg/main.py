import file_ops
from pathlib import Path

workspace = Path("workspace_files")
csv_file = workspace / "students.csv"



name = input("Enter your name: ")
try:
    if name.isalpha():
        print(name)
    else:
        print("enter your name")
except ValueError:
    print("input a name")
age = int(input("enter your age"))
try:
    if age > 0:
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

phone_number = (input("Enter your PhoneNumber: "))
try:
    if len(phone_number) == 11:
        print(phone_number)
    else:
        print("Enter valid number")
except ValueError:
    print("Enter valid number")

contact_info ={
    "name":name,
    "age": age,
    "track": track,
    "phone_number": phone_number
}
# contact_info.update()

# contact_info.save_partcipant()

file_ops.save_participant(csv_file, contact_info)
print('\n Particpant data written to CSV file!')

file_ops.load_partcipants(csv_file)
print('\n Participant data loaded')