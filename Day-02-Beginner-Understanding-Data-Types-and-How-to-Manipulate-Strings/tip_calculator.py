print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people split the bill? "))

print(f"Each person should pay: ${round(((bill / 100 * tip) + bill) / people, 2)}")