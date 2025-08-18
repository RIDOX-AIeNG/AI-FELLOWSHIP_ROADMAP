#Python Operators
# 1.Comparison Operators
# 2.Assignment Operators
# 3.Logical Operators

a = 10
b = 20
print(a==b)
print(a != b)
print(a>b)
print(a < b)
print(a >= 10)
print(b <= 25)

#Use case Example- Student Exam Result
score = 75
print(score >= 50)
print(score < 50)
print(score == 100)

#Assignment Operators
x = 10
print("Initial value: ", x)

x += 5
print("After x += 5:", x)

x -= 2
print("After x *= 3:", x)

x /= 4
print("After x /=4:", x)

x%=3
print("After x %= 3:", x)

x =4
x**=2
print("After x //= 3:", x)

#Use case Example
#Define variables 
balance = 1000
deposit = 200
withdraw = 150

balance += deposit 
balance -= withdraw

print("Updated balance:", balance)
#Output: Updated Balance: 1050

#Logical OPerators
x = 10
y = 20

#and operator
print(x > 5 and y > 15) #True
#or operator
print(x < 5 or y > 15) #True
# not operator
print(not(x == 10))

#Use case example1 - scholarship Eligibility

#Define variables 
age = 17 
score = 85

# Must bwe youner than 18 and score anbove 80
eligible = (age < 18 ) and (score > 80)
print("Scholarship Eligible: ", eligible)
#Output: Scholarship Eligible: True 

#UseCaseExample - Event Access 
age = 22
has_ticket = False

can_center = (age >= 18) and (has_ticket or age < 25)
print("Access Granted:", can_center)