class student: 
    def __init__(self, name, course, level):
        print('Creating a new student...')
        self.name = name
        self.course = course
        self.level = level
        print(f'Student {name} has been created!')

# When you create a student, __init__ runs automatically
kemi = student('Kemi Adebayo', 'Computer Science', 300)

#How Init and Self works together

class NigerianStudent:
    def __init__(self, name, state, course):
        print(f'Step1: Creating student object...')
        self.name = name
        self.state_of_origin = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000, 9999)}"
    
#when you create an object here is what happens:
ayo = NigerianStudent('Ayo Daniel','Lagos', 'Street Statistics')

print(ayo.name)
print(ayo.student_id)

#More example
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f'{self.name} joined {self.network} network')
    def buy_airtime(self, amount):
        self.airtime += amount 
        return f"{self.name} now has ₦{self.airtime} airtime"

#Creating multiple users 
abeeb = PhoneUser('Abeeb Bakare', 'MTN')
onisemo = PhoneUser("Onisemo Williams", "Airtel")

print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(1000))
print(abeeb.airtime)
print(onisemo.airtime)

#ATTRIBUTES

class Student:
    def __init__(self, name , course, level, state_of_origin, cgpa):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = cgpa

#Creating  a student object

Fathia = Student('Fathia Abdul', 'bIOCHEMISTRY', 300, 'Ogun State', 3)
ridwAN = Student('Osho Ridwan', 'Math', 400, 'Ogun', 4.0)
#Acessing attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)
print(Fathia.cgpa)

print(ridwAN.name)
print(ridwAN.course)
print(ridwAN.state_of_origin)
print(ridwAN.cgpa)

#Types of Attributes 

# Instance Attributes - Unique to each object

# student1 = student('Anthony John', 'Engineering', 200, 'Ogun', 9)
# student2 = Student('Fadilat Hassan', 'Medicine', 300, 'Lagos ', 7)

# print(student1)
# print(student2)

#Class Attributes - Shared by all Ojects of the class

class Student:
    university = 'Federal University of Technology Akure'

    def __init__(self, name, course):
        self.name = name
        self.course = course

print(Student.university)
# print(student1.university)
# print(student2.university)

# Methods: The Actions (What Objects Can do)

class Student:
    def __init__(self, name, course, level):
        #Attributes
        self.name = name
        self.course = course
        self.level = level        
        self.cgpa = 0.0
        self.fees_paid = False

    #Method: action the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f'{self.name} has paid school fees for {self.level} level'
    #Method: another action
    def register_courses(self):
        if self.fees_paid:
            return f'{self.name} has registered courses for {self.course} '
        else:
            return f'{self.name} must pay school fees first! '
        
    #Method: calculates CGPA
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
# Using methods 
Abiodun = Student('Abiodun Akinola', 'Gistology', 900)
print(Abiodun.pay_school_fees())
print(Abiodun.register_courses())
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# Types Of Methods
def pay_school_fees(self):
    return f"{self.name} has paid school fees"


# Class Methods
@classmethod
def get_university(cls):
    return cls.university

#Static Method - Don't need object or class data
@staticmethod
def academic_calendar():
    return "academic session runs from september to July"

#How Attributes and Methods Work Together
class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        #ATTRIBUTES - whayt the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    # Methods - what the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount #    Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount #Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
#Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

#Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")

# Methods (actions)
print(adunni_account.deposit(25000))
print(adunni_account.withdraw(10000))
print(adunni_account.transfer(15000, "Sunday James"))
print(adunni_account.check_balance())
        