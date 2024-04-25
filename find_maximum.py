
def find_maximum(numbers):

    numbers = [8, 4, 9, 2, 5, 7, 3]

    maximum = numbers[0]
    
    for numb in numbers:

        if numb > maximum:

            maximum = numb

    return maximum



print(f"Sample Data: {numbers}")

print(f"Expected Output:",find_maximum(numbers))





