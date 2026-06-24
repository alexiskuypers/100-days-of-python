print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
percentage = tip / 100
total_price = bill * percentage + bill

bill_per_person = total_price / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount}.")
