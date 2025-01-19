print("Welcome to tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person_to_split = int(input("How many people to split the bill? "))

total_pay = total_bill + tip / 100 * total_bill
pay_per_person = total_pay / person_to_split

print(f"Each person should pay: ${round(pay_per_person, 2)}")


 