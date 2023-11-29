#if the bill was X, split between 5 people with 12% tip
#Each person should pay (X / 5) * 1.12
#Round the result to 2 decimal places

#Step 1 - Welcome text
print("Welcome to the tip calculator")
#Step 2 - What was the total bill?
total_bill = float(input("What was the total bill? $ \n"))
#Step 3 - What is the percentage of tip would you like to give? 10, 12, or 15?
tip_percentage = int(input("What is the percentage of tip would you like to give?\n"))
#Step 4 - How many people to split the bill?
people_to_split = int(input("How many people to split the bill?\n"))
#Step 5 - Each person should pay:
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
bill_per_person = bill_with_tip / people_to_split
each_person_pay = round(bill_per_person, 2)
each_person_pay = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${each_person_pay}")
