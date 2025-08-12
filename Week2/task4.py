# Creating a life quote, printing in title case and quotation marks.
fave_quote = input("Enter your favorite quote: ").title()
print("\"" + fave_quote + " \"")

#Create a shopping nlist mananger
empty_list = []
list1 = input("enter item: ")
list2 = input("enter item: ")
list3 =input("Enter item: ")
empty_list.append(list1)
empty_list.append(list2)
empty_list.append(list3)
print(",".join(empty_list))

#create a word counter 
sentence = input("enter sentence: ")
print(sentence.split())
print(len(sentence))

# Nmae Organizer
empty_list = []
user1 = input("your name: ").lower()
user2 = input("your name: ").lower()
user3 = input("your name: ").lower()
user4 = input("your name: ").lower()
user5 = input("your name: ").lower()
empty_list.append(user1)
empty_list.append(user2)
empty_list.append(user3)
empty_list.append(user4)
empty_list.append(user5)
empty_list.sort()
print("\n".join(empty_list))




# Create a student score tracker
empty_list1 = []
empty_list2 =[]
sscore1 = input("your score: ")
sscore2 = input("your score: ")
sscore3 = input("your score: ")
sname1 = input("your name: ")
sname2 = input("your name: ")
sname3 = input("your name: ")
empty_list1.append(sscore1)
empty_list1.append(sscore2)
empty_list1.append(sscore3)
empty_list2.append(sname1)
empty_list2.append(sname2)
empty_list2.append(sname3)
print("name\t score")
print("=" * 20)
print(f"{sname1[0]}  \t {sscore1[0]}")
print(f"{sname2[1]} \t {sscore2[1]}")
print(f"{sname3[2]} \t {sscore3[2]}")      

#Word Analyzer
word = input("enter sentence: ")
print(len(word))
is_upper = word.isupper()
is_lower = word.islower()
title = word.istitle()
reversed_word = word[::-1]
print(reversed_word)

# #Cities 
cities = ["beks", "lagos", "oyo","osogbo","abidjan"]
newcity = input("enter your city: ")
cities[2] = newcity
removed_city = cities[:-1]
print(removed_city)
new_city = removed_city.insert(0, "lekki")
print(new_city)