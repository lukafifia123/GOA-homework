def hello_world():
    print("Hello, World!")

# Calling the function
hello_world()


def add_numbers(num1, num2):
    sum_result = num1 + num2
    print("The sum is:", sum_result)

# Calling the function with two numbers
add_numbers(5, 7)



def multiply_by_ten(number):
    result = number * 10
    return result

# Calling the function and printing the result
result = multiply_by_ten(5)
print(result)


def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function with a name
greet("Alice")

# Calling the function without a name (defaults to "Guest")
greet()


def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    inner_function()  # Calling the inner function from within the outer function

# Calling the outer function
outer_function()


def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# Example usage
check_even_odd([1, 2, 3, 4, 5, 6])


def find_maximum(numbers):
    max_num = numbers[0]  # Start by assuming the first number is the maximum
    for num in numbers:
        if num > max_num:  # If the current number is greater than the current max
            max_num = num  # Update max_num to the current number
    return max_num

# Example usage
numbers = [3, 1, 9, 5, 7]
max_value = find_maximum(numbers)
print(f"The maximum number is: {max_value}")


def filter_positive_numbers(numbers):
    positive_numbers = []  # Create an empty list to store positive numbers
    for num in numbers:
        if num > 0:  # Check if the number is positive
            positive_numbers.append(num)  # Add the positive number to the list
    return positive_numbers

# Example usage
numbers = [-10, 5, 0, 8, -3, 7]
positive_numbers = filter_positive_numbers(numbers)
print(f"Positive numbers: {positive_numbers}")


def sum_divisible_by_3(start, end):
    total_sum = 0  # Initialize the sum variable
    for num in range(start, end + 1):  # Iterate through the range
        if num % 3 == 0:  # Check if the number is divisible by 3
            total_sum += num  # Add the number to the total sum
    return total_sum

# Example usage
result = sum_divisible_by_3(1, 100)
print(f"The total sum of numbers divisible by 3 from 1 to 100 is: {result}")








