cutOff_Mark = 180 #cutoff mark
Student_Result = int(input("Enter score:"))#Student result

try:
    if  (cutOff_Mark == Student_Result):
        print('student is admitted')
    elif(cutOff_Mark < Student_Result):
        print(f"student is admitted") 
    elif(cutOff_Mark > Student_Result):
        print("student is not admmitted")
except ValueError:
    print("invalid input enter a number" )