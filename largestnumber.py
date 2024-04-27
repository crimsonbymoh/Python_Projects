def largest(number1, number2, number3):

	largest_number = number1

	if number2 > largest_number:
 		largest_number = number2
	if number3 > largest_number:
		largest_number = number3

	return largest_number

def smallest(number1, number2, number3):

	smallest_number = number1

	if number2 < smallest_number:
 		smallest_number = number2
	if number3 < smallest_number:
		smallest_number = number3

	return smallest_number
