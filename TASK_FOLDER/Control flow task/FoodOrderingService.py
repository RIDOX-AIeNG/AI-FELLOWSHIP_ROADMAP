#This is a food ordering app,like chowdeck and the likes.

#This welcomes the user to the app
print("THIS IS RIDOX'S BITE") 

#This allows the user to input their login details as it is originally stored in the database.

username = input("enter your username:")
password = input("enter your password:")

#I used an if statement as a control flow mechanism. such that if the user enters their correct details it takes them straight to the ordering page or menu.
if username == "McMaggie" and password == "1234":

#this is the ordering menu/page
    print(f"Welcome {username}")
    print(f'{username} what would you like to order? ')
    print("\nMenu ")
    print("1. Pizza")
    print("2. Sharwama")
    print("3. Meat Pie")
    print("4. Fish Pie")

#Created this dictionary with the options as the key and food items as the value. so the order output can recognize the food item.
    dic = {'1': "Pizza", '2':"Sharwama", '3':"Meat Pie", '4':"Fish Pie"}

    choice = input("Enter choice: ")
    
    if choice == "1":
       print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "2":
        print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "3":
        print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "4":
        print(f"Your {dic[choice]} will be ready in a jiffy")

elif username == "Ridwan" and password == "5678":

    print(f"Welcome {username}")
    print(f'{username} what would you like to order? ')
    print("\nMenu ")
    print("1. Pizza")
    print("2. Sharwama")
    print("3. Meat Pie")
    print("4. Fish Pie")

    dic = {'1': "Pizza", '2':"Sharwama", '3':"Meat Pie", '4':"Fish Pie"}

    choice = input("Enter choice: ")
    
    if choice == "1":
       print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "2":
        print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "3":
        print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "4":
        print(f"Your {dic[choice]} will be ready in a jiffy")

elif username == "Victor" and password == "91011":

    print(f"Welcome {username}")
    print(f'{username} what would you like to order? ')
    print("\nMenu ")
    print("1. Pizza")
    print("2. Sharwama")
    print("3. Meat Pie")
    print("4. Fish Pie")

    dic = {'1': "Pizza", '2':"Sharwama", '3':"Meat Pie", '4':"Fish Pie"}

    choice = input("Enter choice: ")
    
    if choice == "1":
       print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "2":
        print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "3":
        print(f'Your{dic[choice]} will be ready in a jiffy')
    elif choice == "4":
        print(f"Your {dic[choice]} will be ready in a jiffy")
        
else:
  print("invalid username or password")




