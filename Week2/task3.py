name = input("Full name:") #collect name from user
print(f"My names are {name.upper()} ") # print the name in capital

tag = "python" #give the variable a value
print(tag[0]) #print the first letter
print(tag[-1]) #print the last letter

user_name = input("Your Name: ") # collects users name
print(f"Hello! {user_name}") # print a function that greets the user

character = "ridwan"
print(character.find(character[-1])+1) 

text = "Hello World"
print(text.replace("World","python"))

text = "My names are Ridwan python"
print("python" in text)


word = "Ayomide"
print(''.join(reversed(word)))

word = "  Ayomide   "
print(word.lstrip().rstrip())

text = input("enter your full name: ")
less = text.count('a')+ text.count('e')+ text.count('i')+ text.count('o') + text.count('u')
print(less)

string = "1234"
print(int(string)*2)

