print("WElcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What is the percentage of tip you wanna give? (10, 12 or 15) "))
num_ppl = int(input("Enter number of people to split among: "))

amt = round((total_bill* (1+(tip_percent/100)))/num_ppl,2)

print(f"Each person should pay ${amt}")