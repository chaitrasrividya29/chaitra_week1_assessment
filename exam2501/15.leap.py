def is_leap(year):
    if(year%4==0):
        print(f"{year} IS A LEAP YEAR""\n")
    else:
        print(f"{year} IS NOT A LEAP YEAR""\n")
    return
def main():
    t=True
    while(t):
        ch=int(input("CHOOSE AN OPTION \n1. GIVE YEAR \n2. EXIT\n"))
        if(ch==2):
            t=False
        else:
            year=int(input("ENTER THE YEAR:"))
            is_leap(year)

main()