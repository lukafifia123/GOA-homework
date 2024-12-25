# სამი რიცხვის მიღება მომხმარებლიდან
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = float(input("შეიყვანეთ მესამე რიცხვი: "))

# ყველაზე დიდი რიცხვის მოძებნა if-elif-else-ით
if num1 >= num2 and num1 >= num3:
    print(f"ყველაზე დიდი რიცხვია {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"ყველაზე დიდი რიცხვია {num2}")
else:
    print(f"ყველაზე დიდი რიცხვია {num3}")




# Take a number as input from the user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")





# Take two integers as input from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialize a variable to hold the sum
total_sum = 0

# Use a for loop to calculate the sum of numbers from start to end (inclusive)
for num in range(start, end + 1):
    total_sum += num

# Print the result
print(f"The sum of numbers between {start} and {end} is {total_sum}")





# Take a number as input from the user
num = int(input("Enter a number: "))

# Check if the number is less than 2 (since prime numbers are greater than 1)
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Assume the number is prime
    is_prime = True
    
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # Output the result
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")





# Create a list of five numbers
numbers = [10, 20, 30, 40, 50]

# Print the first, third, and last elements using indexing
print("First element:", numbers[0])   # First element is at index 0
print("Third element:", numbers[2])   # Third element is at index 2
print("Last element:", numbers[-1])   # Last element is at index -1





# Create a list with 20 elements of various data types
elements = [42, "hello", 3.14, True, [1, 2, 3], {"key": "value"}, None, 99, "world", 56.78, 
            False, (5, 6), {10, 20}, 123, "Python", 7, 8.9, 100, 200, 300, "end"]

# Print all elements using indexing
for i in range(len(elements)):
    print(f"Element at index {i}: {elements[i]}")



















