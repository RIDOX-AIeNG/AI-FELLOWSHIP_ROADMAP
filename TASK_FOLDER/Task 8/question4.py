#Student Record
student = {}
name = input("enter your name: ")
Age = int(input("Enter your age: "))
student["name"] = name
student["age"] = Age
scores = [34,56,79]
student["score"] = scores
average = sum(scores)/len(scores)
student["passed"] = average >= 50
student["Teenage"]= (Age >= 13) and (Age < 19)
print(f"student Record\nname: {student['name']}\nAge: {student["age"]}\nScore: {student["score"]}\nPassed:{student["passed"]}\nTeenage: {student["Teenage"]}")

