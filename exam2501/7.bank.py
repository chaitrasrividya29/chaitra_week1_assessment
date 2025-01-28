def check_eligible(salary,age,credit_score):
    if(salary>=50000):
        if(age>20):
            if(credit_score>700):
                print("!!!APPROVED!!! \nTHE CANDIDATE MATCHES ALL THE REQUIREMENTS.")
            else:
                print("!!!REJECTED!!! \nTHE CANDIDATE HAVE THE SALARY AND THE REQUIRED AGE BUT DOES NOT HAVE THE CREDIT SCORE.")
        else:
            print("!!!REJECTED!!! \nTHE CANDIDATE HAVE THE SALARY BUT DOES NOT HAVE THE REQUIRED AGE.")    
    else:
        print("!!!REJECTED!!! \nSALARY OF THE CANDIDATE IS NOT SUFFICIENT.")
    return 

def main():
    salary=int(input("ENTER THE SARARY OF THE CANDIDATE: "))
    age=int(input("ENTER THE AGE OF THE CANDIDATE: "))
    credit_score=int(input("ENTER THE CREDIT SCORE OF THE CANDIDATE: "))
    check_eligible(salary,age,credit_score)

main()