accepted_weight = 180
age = 30

user_name = input('Ënter your name: ')

user_weight = int(input('Enter your height: ')) 

user_age = int(input("Enter your age: "))
try:
    if (user_weight >= accepted_weight) and (user_age >= age):

        print(f"{user_name} is eligible ")
    else:
        print(f"{user_name} is not eligible.")
except ValueError:
    print("Invalid input, enter a number")