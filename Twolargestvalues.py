largest = 0
second_largest = 0

for i in range(10):

	number = int(input("Enter number: "))

	if number > largest:

		second_largest = largest

		largest = number

	elif number > second_largest:

		second_largest = number 

print("The largest number is:", largest)

print("The second largest number is:", second_largest)