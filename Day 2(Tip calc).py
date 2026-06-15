print("Welcome to tip calculator!")
amount=int(input("What is the total bill?"))
people=int(input("How many people are there to split the bill?"))
percentage=int(input("What is the percentage of tip you guys would like to give?"))
tot_amt=amount+(amount*(percentage/100))
amt_pp=tot_amt/people
print(f"Amt per person is:{amt_pp}")
print("Thank you for your time!")
