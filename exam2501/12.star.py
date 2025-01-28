n = int(input("Enter a number: "))
for i in range(1, n+1):
    print('*' * i)
x=int(input("do you want to reverse the pattern. If yes enter 1 and 0 for exit."))
if(x==1):
    for i in range(n,0,-1):
        print("*"*i)