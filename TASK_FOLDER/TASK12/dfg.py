email = input('Enter email address')

if email == "":
    print("INput your email address")
elif email !="":
    print("Email added succcessfully")
if "@" in email:
 email_split = email.split("@")
 user_name = email_split[0]
 domain = email_split[1]
 print(user_name, domain)