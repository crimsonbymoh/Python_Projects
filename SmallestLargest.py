number1 = int(input("Enter the first number: "))

number2 = int(input("Enter the second number: "))

number3 = int(input("Enter the third number: "))

sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3 

smallest = 0
largest = 0

print("Sum: ", sum)

print("Average: ", average)

print("product: ", product)

if number1 < number2 and number1 < number3:
	
	print("The Smallest number is: ", number1)

if number2 < number1 and number2 < number3:
	
	print("The Smallest number is: ", number2)

if number3 < number1 and number3 < number1:

	print("The Smallest number is: ", number3)


if number1 > number2 and number1 > number3:

	print("The Largest number is: ", number1)

if number2 > number1 and number2 > number3:

	print("The Largest number is: ", number2)

if number3 > number1 and number3 > number2:

	print("The Largest number is: ", number3)
	