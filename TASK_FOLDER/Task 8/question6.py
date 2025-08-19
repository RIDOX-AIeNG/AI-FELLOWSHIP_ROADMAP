name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Utme_score = int(input("Enter your Utme score: "))
post_utme_score = int(input("Enter postUtme Score: "))
Institution = input("Enter your choice of institution: ")
departmental_cut_off= (Utme_score+post_utme_score)/2
# SUBJECTS
print("Enter Grades for Wassce Subjects")
grades=[]
english= input("Enter your grade for English: ").upper()
mathematics= input("Enter your grade for mathematics: ").upper()
subject_3= input("Enter your grade for subject 3: ").upper ()
subject_4= input("Enter your grade for subject 4: ").upper()
subject_5= input("Enter your grade for subject 5: ").upper()
grades.append(english)
grades.append(mathematics)
grades.append(subject_3)
grades.append(subject_4)
grades.append(subject_5)

eligibility= (Age >= 16) and(Utme_score >= 200) and (post_utme_score>=50) and ( departmental_cut_off>=50) and(Institution=="UNILAG" ) and set(grades) <= {"a","b","c"}
