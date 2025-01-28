
 
print("Temperature Conversion:")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")
print("4: Kelvin to Celsius")
print("5: Fahrenheit to Kelvin")
print("6: Kelvin to Fahrenheit")
    
choice = int(input("Choose an option (1-6): "))
    
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}C = {fahrenheit:.2f}F")
    
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}F = {celsius:.2f}C")
    
elif choice == 3:
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}C = {kelvin:.2f} K")
 
elif choice == 4:
    kelvin = float(input("Enter temperature in Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin} K = {celsius:.2f}C")
 
elif choice == 5:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print(f"{fahrenheit}F = {kelvin:.2f} K")
 
elif choice == 6:
    kelvin = float(input("Enter temperature in Kelvin: "))
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"{kelvin} K = {fahrenheit:.2f}F")
 
else:
    print("Invalid option!")
 