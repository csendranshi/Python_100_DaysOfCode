height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")
bmi = int(float(weight)/(float(height)**2))

if bmi>=35:
    print("Clinically obese")
elif bmi>=30:
    print("Obese")
elif bmi>=25:
    print("OverWeight")
elif bmi>=18.5:
    print("Normal Weight")
else:
    print("Underweight")