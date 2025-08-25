print("Welcome to Ridox Telecommunication services")
balance = 5000

while True: 
    try:
        print("\nServices Available: ")
        print("\n1. Purchase Airtime")
        print("\n2. Buy data")
        print("\n3. Pay Electricity Bill")
        print("\n4. Pay for TV subsricption")
        print("\n5. Exit program")

        choice = input("Enter choice: ")
        
        if choice == "1":
            print("1. Buy for yourself")
            print("2. Buy for a friend")

            choice = input("enter choice: ")
            if choice == "1":
                amount = int(input("Enter amount: "))
                if amount <= balance:
                    print("Airtime purchased successfully")
                    balance -= amount
                    print(f"New balance is {balance}₦ ")
                else:
                    print("Balance is insufficient")
            elif choice == "2":
                amount = int(input("Enter amount: "))
                if amount <= balance:
                    print("Airtime purchased successfully")
                    balance -= amount
                    print(f"New balance is {balance}₦ ")
        elif choice == "2":
            print("Select Bundle")
            print("1. 200# for 1gb")
            print("2. 500# for 2.5gb")
            print("3. 1000# for 5gb ")

            choice = input("enter choice: ")
            if choice == "1":
                amount = int(input("Enter amount: "))
            if amount <= balance:
                print('data purchased successfully')
            elif choice == "2":
                amount = int(input("Enter amount: "))
            if amount <= balance:
                print('data purchased successfully')
            elif choice == "3":
                amount = int(input("Enter amount: "))
                if amount <= balance:
                    print('data purchased successfully')
        elif choice == "3":
            print("Purchase @ 150# per unit ")
            unit = float(input("Enter unit: "))
            price = unit * 150
            if price <= balance:
                print(f'you have purchased {price}# of power ')
                balance -= price
                print(f"your new balance is {balance}₦")
                print('Thank you for using our service')
        elif choice == "4":
            print("Select Provider")
            print("1. DSTV")
            print("2. GOtv")
            print("3. Startimes")

            choice = input("Enter choice: ")
            if choice == "1":
                dic = {'Premium': 4000, 'Compact': 2500, 'Naija Padi': 1500}
                print("Select Package")
                print("1. Premium")
                print("2. Compact")
                print("3. Naija Padi")

                choice = input("Enter choice: ")
                if choice == "1":
                    if dic['Premium'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Premium']
                        print(f'Your balance is {balance}₦')
                    else:
                        print("Balance not sufficient")
        
                elif choice == "2":
                    if dic['Compact'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Compact']
                        print(f'Your balance is {balance}₦')
                    else:
                        print('balance not sufficient')
                elif choice == "3":
                    if dic['Naija Padi'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Naija Padi']
                        print(f'Your balance is {balance}₦')
                    else:
                        print("balance not sufficient")
            elif choice == "2":
                dic = {'Jinja': 4000, 'Jollie': 2500, 'Smallie': 1500}
                print("Select Package")
                print("1. Jinja")
                print("2. Jollie")
                print("3. Smallie")

                choice = input("Enter choice: ")
                if choice == "1":
                    if dic['Jinja'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Jinja']
                        print(f'Your balance is {balance}₦')
                    else:
                        print("Balance not sufficient")
        
                elif choice == "2":
                    if dic['Jollie'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Jollie']
                        print(f'Your balance is {balance}₦')
                    else:
                        print('balance not sufficient')
                elif choice == "3":
                    if dic['Smallie'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Smallie']
                        print(f'Your balance is {balance}₦')
                    else:
                        print("balance not sufficient")
            elif choice == "3":
                dic = {"Nova": 3000, "Basic": 2300, "Super": 1700}
                print("Select Package")
                print("1. Nova")
                print("2. Basic")
                print("3. Super")

                choice = input("Enter choice: ")
                if choice == "1":
                    if dic['Nova'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Nova']
                        print(f'Your balance is {balance}₦')
                    else:
                        print("Balance not sufficient")
        
                elif choice == "2":
                    if dic['Basic'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Basic']
                        print(f'Your balance is {balance}₦')
                    else:
                        print('balance not sufficient')
                elif choice == "3":
                    if dic['Super'] <= balance:
                        print('package purchased successfully')
                        print("Restart your decoder to effect change")
                        balance -= dic['Super']
                        print(f'Your balance is {balance}₦')
                    else:
                        print("balance not sufficient")
        elif choice == "5":
            print("Thank you for using our service😁")
            break
        else:
            print("Invalid input,try again.")
    except ValueError:
        print("Invalid input,enter a number")






                