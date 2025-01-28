
# 4. Student Grading System
 
import numpy as np 
 
def grade(per):
    if(per>90):
        print("GRADE: A")
    elif(80< per <90):
        print("GRADE: B")
    elif(70 < per<80):
        print("GRADE: C")
    elif(45< per <70):
        print("GRADE: D")
    else:
        print("GRADE: FAIL")
        
def percentage(total,max_marks):
    per=(total/max_marks)*100
    print(f"PERCENTAGE OBTAINED:{per}")
    return per
 
def total_m(arr_marks):
    total=sum(arr_marks)
    print(f"TOTAL MARKS OBTAINED: {total}")
    return total 
 
name=input("enter name: ")
max_marks=int(input("enter max marks for each subject: "))
arr_marks=[]
for i in range(5):
    marks=int(input(f"enter marks of subject {i+1} "))
    arr_marks.append(marks)
tot=total_m(arr_marks)
percent=percentage(tot,max_marks*5)
grade(percent) 