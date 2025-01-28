numbers=list(map(int, input("enter numbers: ").split()))
odd=[]
even=[]
for num in numbers:
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)
print("even:",even)
print("odd:",odd)