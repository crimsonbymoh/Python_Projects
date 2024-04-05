print('number\tsquare\tcube')

number = 0
square = 0
cube = 0

for number in range(0,6):
	square = number * number
	cube = number * number * number

	print(f'{number}\t{square}\t{cube}')