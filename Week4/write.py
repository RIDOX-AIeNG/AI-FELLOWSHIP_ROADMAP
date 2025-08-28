from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"
file_path


# (A) Create or overwrite using 'w'
f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()

# #(B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()


# f = open(file_path, "w", encoding="utf-8")
# f.write("Shopping List:\n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()

# f = open(file_path, "r", encoding="utf-8")
# content = f.read()
# f.close()
# print(content)

# f = open(file_path, "r", encoding="utf-8")
# lines = f.readlines()
# f.close()
# print("Lines list:", [line.strip() for line in lines])
# # print(f"Lines list: {lines}")

# f = open(file_path, "r", encoding="utf-8")
# for line in f:
#     print("->", line.rstrip())
# f.close()

# import json
# from pathlib import Path

# workspace = Path("workspace_files")

# # Create some student data (like a mini database)
# student_data = {
#     "name": "Oyindamola",
#     "age": 16,
#     "courses": ["Python", "Data Science", "Web Development"],
#     "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
#     "is_graduated": False
# }

# # Save the data to a JSON file
# json_file = workspace / "student_data.json"
# with open(json_file, "w", encoding="utf-8") as f:
#     json.dump(student_data, f, indent=2)  # indent=2 makes it pretty and readable

# print("Student data saved to JSON file!")

# # Now read it back
# with open(json_file, "r", encoding="utf-8") as f:
#     loaded_data = json.load(f)

# print("\nData read from JSON file:")
# print(f"Student name: {loaded_data['name']}")
# print(f"Age: {loaded_data['age']}")
# print(f"Courses: {', '.join(loaded_data['courses'])}")
# print(f"Python grade: {loaded_data['grades']['Python']}")
# print(f"Data Science grade: {loaded_data['grades']['Data Science']}")

import csv
from pathlib import Path

workspace = Path("workspace_files")
csv_file = workspace / "students.csv"

# Create sample student data
students = [
    ["Name", "Age", "Course", "Grade"],  # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

# Write data to CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students[:])  # Write all rows at once

print("Student data written to CSV file!")

# Read the CSV file back
print("\nReading CSV file:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    for row_number, row in enumerate(reader):
        if row_number == 0:  # Header row
            print(f"Headers: {' | '.join(row)}")
            print("-" * 40)
        else:  # Data rows
            name, age, course, grade = row
            print(f"{name} ({age} years) - {course}: {grade}")