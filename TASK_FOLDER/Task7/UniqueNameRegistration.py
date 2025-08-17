#Unique Name Registration
#Ask user to input 3 names separated by commas
#Covert the input to a set
#Use dictionary comprehension[counts its length]
name_entry = input("Please enter 3 names separated by commas: ").split(", ")
name_entry = set(name_entry)
name_dict = {name: len(name) for name in name_entry}
print(name_dict)