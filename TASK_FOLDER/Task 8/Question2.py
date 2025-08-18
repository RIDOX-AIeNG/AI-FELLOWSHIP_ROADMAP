# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

#Explanation
# The code is collecting the user details such as the age, name, score to check if the user is eligible 

#Federal Government Scholarship Key Eligibilty Status
Name = input("Enter your name: ")
Citizenship = input("Enter your natinality: ").lower()
Employment_status = input("Enter your employment status(Undergrad/Grad/employed): ").lower()
Scholarship_Enrolled = input("Are you enrolled in any scholarship: ").lower()
Academic_subject = input("enter 5 subjects separated by commas: ").split(",")
academic_qualification = [input(f"Enter grade for {subject}: ") for subject in Academic_subject]
print(academic_qualification)
accepted_grade = ("A" in academic_qualification) or ("B" in academic_qualification)
print(f"accepted grade {accepted_grade}")
eligibility = (Citizenship == "nigerian") and (Employment_status == "undergraduate") and (Scholarship_Enrolled == "no") and (accepted_grade == True)

print(f"Candidate:{Name}\nCitizenship:{Citizenship}\nEmployment Status:{Employment_status}\nEnrollment: {Scholarship_Enrolled}\nEligible: {eligibility}")