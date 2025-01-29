# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function to calculate the sum
result = sum_of_two_numbers(num1, num2)

# Printing the result
print("The sum of", num1, "and", num2, "is:", result)




def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Taking input from the user
number = int(input("Enter an integer: "))

# Calling the function to determine if the number is even or odd
result = even_or_odd(number)

# Printing the result
print("The number", number, "is", result)



def reverse_string(s):
    return s[::-1]


# Taking input from the user
s = input("Enter a string: ")

# Calling the function to reverse the string
reversed_s = reverse_string(s)

# Printing the reversed string
print("Reversed string:", reversed_s)


def find_maximum(numbers):
    return max(numbers)



# Taking input from the user as a list of numbers
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Calling the function to find the maximum value
max_value = find_maximum(numbers)

# Printing the maximum value
print("The maximum value is:", max_value)



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



# Taking input from the user
n = int(input("Enter a number to calculate its factorial: "))

# Calling the function to calculate the factorial
result = factorial(n)

# Printing the result
print(f"The factorial of {n} is: {result}")




























