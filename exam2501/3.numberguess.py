import random

rand= random.randrange(1,100)
number=0
while(True):
    number=int(input("enter number: "))
    diff=abs(rand-number)
    if(diff==0):
        print("number found")
        break
    elif(diff>90 and diff<100):
        print("too high")
    elif(diff>70 and diff<90):
        print("too low")
    elif(diff<10):
        print("you are almost there")
    else:
        continue







