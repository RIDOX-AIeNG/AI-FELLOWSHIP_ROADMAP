#This is to check for eligibility of candidates for heavyweights.

accepted_weight = 160 
age = 25

user_name = input('Ënter your name: ')

user_weight = int(input('Enter your height: ')) 

user_age = int(input("Enter your age: "))

if (user_weight >= accepted_weight) and (user_age >= age):

    print(f"{user_name} is eligible ")
else:
    print(f"{user_name} is not eligible.")