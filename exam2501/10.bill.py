def tip_calculator(bill,tip):
    res=(bill/100)*10
    return res

def split_calculator(bill,number,tip):
    total=bill+tip
    split=total/number
    print(f"EACH PERSON HAVE TO PAY {split}")
    return

def main():
    bill=int(input("enter the bill amount: "))
    number=int(input("enter the number of persons: "))
    tip=int(input("enter the tip percent you want to add range(0%-15%): "))
    tip=tip_calculator(bill,tip)
    split_calculator(bill,number,tip)

main()
