#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_as_int = int(tip * .01 * bill)
share = (bill + tip_as_int) / people

#Format the result to 2 decimal places = 33.60
print(round(share, 2))
