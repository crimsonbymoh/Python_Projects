principal_amount = int(input("Enter Principal Amount: "))

rate = float(input("Enter Annual Rate of return: "))

number_of_years = int(input("Enter the number of years: "))

amount = principal_amount * (1 + rate) ** number_of_years

print("The Amount After " + str(number_of_years) + " years: ", amount)

