num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} == {num2} : {num1 == num2}") #This is checking if the numbers are equal
print(f"{num1} != {num2} : {num1 != num2}")#This is checking if the numbers are not equal
print(f"{num1} > {num2} : {num1 > num2}")#This is checking if the numbers are greater than another
print(f"{num1} < {num2} : {num1 < num2}")#This is checking if gthe number is less than another

#Use Cases
#1. Student admission
#2. Temperature Measure
#3. Competency Test

#Student admission
cutOff_Mark = 180 #cutoff mark
Student_Result = int(input("Enter score:"))#Student result

print(f"Student is admitted : {cutOff_Mark == Student_Result}")
print(f"student is not admitted : {cutOff_Mark != Student_Result}") 
print(f"student is not admitted: {cutOff_Mark < Student_Result}") 
print(f"student is admitted: {cutOff_Mark > Student_Result}") 