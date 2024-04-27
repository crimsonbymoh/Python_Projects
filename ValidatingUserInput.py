no_of_students = 10

no_of_students_passed = 0

no_of_students_failed = 0

for _ in range(no_of_students):

	result = 0

	while result not in [1, 2]:

		result = int(input("Enter result(1= pass, 2= fail): "))

	if result == 1:

		no_of_students_passed  = no_of_students_passed  + 1

	else:

		no_of_students_failed = no_of_students_failed + 1

print("passed: ", no_of_students_passed)

print("failed: ", no_of_students_failed)

if no_of_students_passed > 8:

	print("Bonus To Instructor")