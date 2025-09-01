def email_slicer(email):
    
    if "@" in email and '.' in email.split('@')[1]:
       
        username, domain = email.split('@')
        return username, domain
    else:
        
        return None, None


email = input("Enter your email address: ")


username, domain = email_slicer(email)


if username and domain:
    print(f"Username: {username}\nDomain: {domain}")
else:
    print("Invalid email format! Please enter a valid email.")