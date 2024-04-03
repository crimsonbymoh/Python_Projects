number1 = float(input("Enter the first number: "))

number2 = float(input("Enter the second number: "))

number3 = float(input("Enter the third number: "))

if number1 < number2 and number1 < number3:

	smallest = number1

	if number2 < number3:

	  middle = number2
 
	  largest = number3

	else:
		middle = number3

		largest = number2

if number2 < number1 and number2 < number3:

	smallest = number2

	if number1 < number3:

	  middle = number1 
	
	  largest = number3

	else: 
		middle = number3

		largest = number1 

if number3 < number1 and number3< number2 :

	smallest = number3

	if number1 < number2:

	  middle = number1 
	
	  largest = number2

	else: 
		middle = number2

		largest = number2
	




print("The numbers in increasing order are: ", smallest , middle , largest)

	