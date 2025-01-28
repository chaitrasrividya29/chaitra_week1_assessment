def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18:
        return "Underweight"
    elif 18.5 <= bmi < 24:
        return "Normal weight"
    elif 25 <= bmi < 29:
        return "Overweight"
    else:
        return "Obese"


weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = calculate_bmi(weight, height)


print(f"Your BMI is: {bmi}")
print(f"Your BMI category is: {categorize_bmi(bmi)}")