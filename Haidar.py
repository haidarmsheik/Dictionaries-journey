salary = int(input ("please input your salary :") )
month = input("please input the month : " )
savingsPercentage = int(input("please enter the percentage of savings :" ) )
rentPercentage = int(input("please enter the percentage of rent :") )
electricityPercentage = int(input("please enter the percentage of electricity :") )

savings = (savingsPercentage / 100) * salary
rent = (rentPercentage / 100) * salary
electricity = (electricityPercentage / 100) * salary

totalAmount = savings + rent + electricity

remainder = salary - totalAmount

yearlyRent = rent * 12
yearlyElectricity = electricity * 12

salaryPowered = salary ** 2

additionalSavings = float(input("please enter the amount of addtitional savings :") )
totalAdditionalsavings = additionalSavings / savings

print("\n--- Monthly Financial Summary for", month, "---")
print(f"Savings: {savings}")
print(f"Rent: {rent}")
print(f"Electricity: {electricity}")
print(f"Total Expenses: {totalAmount}")
print(f"Remainder: {remainder}")
print(f"Yearly Rent: {yearlyRent}")
print(f"Yearly Electricity: {yearlyElectricity}")
print(f"Salary Powered: {salaryPowered}")
print(f"Additional Savings: {additionalSavings}")
print(f"total Additional savings: {totalAdditionalsavings}")