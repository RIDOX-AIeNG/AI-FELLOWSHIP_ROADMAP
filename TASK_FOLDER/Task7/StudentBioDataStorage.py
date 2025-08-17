#creating a student bio data storage
# Create an input function for the name, age, gender and course
#Then store the course in a list
#Then add the whole data in a dictonary
#Then display the bio-data neatly using escape sequences 
name = input("Enter your name: ")
age = input("Ënter your age: ")
gender = input("Enter your gender: ")
courses = input("Enter your course: ")
ls_course = list(courses)
student_bio = {
    "name": name,
    "age": age,
    "gender": gender,
    "course": ls_course
}
print(f"student information \n================ \nName = {name}\nAge = {age}\nGender = {gender}\nCourses = {ls_course}")