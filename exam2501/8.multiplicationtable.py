def tabel(number,r):
    for i in range(r+1):
        print(f"{number} x {i} = {number*i}""\n")
    return
def main():
    number=int(input("enter the number: "))
    r=int(input("enter the range: "))
    tabel(number,r)
main()