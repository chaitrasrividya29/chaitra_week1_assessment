def find_second_large(numbers):
    var_numbers=list(set(numbers))
    if(len(var_numbers)<2):
        return null
    var_numbers.sort(reverse=True)
    return var_numbers[1]

numbers=list(map(int,input("enter numbers: ").split()))
res=find_second_large(numbers)
print(f"second largest number is:{res}")