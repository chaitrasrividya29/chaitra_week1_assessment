
 
# 5.shopping cart
 
print("WELCOME TO THE MART")
cart={}
items=[]
costs=[]
t=True
while t:
    ch=int(input("1.ADD ITEM\n\n2.EXIT\nENTER YOUR CHOICE:"))
    if ch == 1:
        item=input("enter the name of product: ")
        items.append(item)
        cost=int(input("enter the cost of the product: "))
        costs.append(cost)
        cart[item]=cost
    elif ch==2:
        break
    else:
        print("give a valid input!!")
print("items in cart",cart)
res=sum(costs)
print("total cost of the cart: ",res)