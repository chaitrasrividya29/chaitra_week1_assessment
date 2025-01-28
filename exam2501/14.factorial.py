#factorial program

def factorial(rang):
    fact=1
    for i in range(2,rang+1):
        fact *= i
    print(f"THE FACTORIAL OF {rang} IS: {fact}")
    return

def main():
    rang=int(input("enter the range: "))
    if(rang<0):
        print("negative range")
        rang=int(input("enter a positive value: "))
    else:
        print(1)
        factorial(rang)
    
main()