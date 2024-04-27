
import random

LUCKY_NUMBER = random.randrange(1, 10)

print("Welcome To My Games")

number = 0


while number != LUCKY_NUMBER:

	number = int(input("Enter A Number: "))

	if number != LUCKY_NUMBER:

		print('Try Again')

	else:
		print('You are correct!!')

		break
