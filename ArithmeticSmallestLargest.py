numbers = []
for i in range(4):

	number = int(input(f"Enter  Number {i + 1}: "))

total_sum = sum(numbers )

average = total_sum / 4

smallest_number = min(numbers)

largest_number = max(numbers)

print("Sum: ", total_sum)

print("Average: ", average)

print("Smallest: ", smallest_number)

print("Largest: ", largest_number)

