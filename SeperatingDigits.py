number_string = input('Enter a 5 digit Integer: ')

number = int(number_string)

first_digit = number % 10
number = number // 10

second_digit = number % 10
number = number // 10

third_digit = number % 10
number = number // 10

fourth_digit = number % 10
number = number // 10

fifth_digit = number % 10
number = number // 10

print(fifth_digit, fourth_digit, third_digit, second_digit, first_digit, sep="   ")