passed = 0
failed = 0
pass_mark = 45

for  i in range(1, 16):

	score = int(input("Enter Score Of Student: "))

	if score >= pass_mark:

		  passed += 1

	else: 
		
		  failed += 1

print("\nThe Number Of Students Who Passed is: ", passed )

print("The Number Of Students Who Failed is: ", failed )

