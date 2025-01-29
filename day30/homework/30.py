# Given sentence
sentence = "This is a sample sentence."

# Convert the sentence to uppercase
uppercase_sentence = sentence.upper()

# Print the result
print(uppercase_sentence)



# Take user's name as input
user_name = input("Enter your name: ")

# Convert the name to uppercase
uppercase_name = user_name.upper()

# Display the result
print("Your name in uppercase is:", uppercase_name)



def convert_to_uppercase(str_list):
    # Convert each string in the list to uppercase
    return [s.upper() for s in str_list]

# Example usage
lowercase_list = ["apple", "banana", "cherry"]
uppercase_list = convert_to_uppercase(lowercase_list)

# Display the result
print(uppercase_list)



# Given sentence
sentence = "This Is A Sample Sentence."

# Convert the sentence to lowercase
lowercase_sentence = sentence.lower()

# Print the result
print(lowercase_sentence)



# Ask the user for their email address
email = input("Please enter your email address: ")

# Convert the email address to lowercase
email_lowercase = email.lower()

# Print the result
print("Your email address in lowercase is:", email_lowercase)


def to_lowercase(input_string):
    # Convert the string to lowercase and return it
    return input_string.lower()

# Example usage
mixed_case_string = "ThIs Is A MiXeD CaSe StRiNg"
lowercase_string = to_lowercase(mixed_case_string)

# Display the result
print(lowercase_string)


# Ask the user for a sentence
sentence = input("Please enter a sentence: ")

# Capitalize the first letter of the sentence
capitalized_sentence = sentence.capitalize()

# Display the result
print("Capitalized sentence:", capitalized_sentence)


def capitalize_first_letter(str_list):
    # Capitalize the first letter of each string in the list
    return [s.capitalize() for s in str_list]

# Example usage
lowercase_strings = ["apple", "banana", "cherry"]
capitalized_strings = capitalize_first_letter(lowercase_strings)

# Display the result
print(capitalized_strings)


def capitalize_first_letter(input_string):
    # Capitalize the first letter of the string and return it
    return input_string.capitalize()

# Example usage
input_string = "hello world"
capitalized_string = capitalize_first_letter(input_string)

# Display the result
print(capitalized_string)


def find_python_position(sentence):
    # Find the position of the first occurrence of the word 'Python'
    position = sentence.find("Python")
    
    # Check if 'Python' is found and print the result
    if position != -1:
        print(f"The word 'Python' is found at index {position}.")
    else:
        print("The word 'Python' is not found in the sentence.")

# Example usage
sentence = input("Enter a sentence: ")
find_python_position(sentence)



def find_substring_index(main_string, substring):
    # Find the starting index of the substring in the main string
    index = main_string.find(substring)
    
    # If the substring is found, return the index, otherwise indicate it's not found
    if index != -1:
        print(f"The substring '{substring}' starts at index {index}.")
    else:
        print(f"The substring '{substring}' was not found.")

# Example usage
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

find_substring_index(main_string, substring)


def find_python_position(sentence):
    # Find the position of the first occurrence of the word 'Python'
    position = sentence.find("Python")
    
    # Check if 'Python' is found and print the result
    if position != -1:
        print(f"The word 'Python' is found at index {position}.")
    else:
        print("The word 'Python' is not found in the sentence.")

# Example usage
sentence = input("Enter a sentence: ")
find_python_position(sentence)


def find_character_index(input_string, character):
    # Find the index of the specified character in the string
    index = input_string.find(character)
    
    # Return the index if the character is found, else return -1
    return index

# Example usage
input_string = input("Enter a string: ")
character = input("Enter the character to search for: ")

index = find_character_index(input_string, character)

if index != -1:
    print(f"The character '{character}' is found at index {index}.")
else:
    print(f"The character '{character}' is not found in the string.")


# Ask the user for a string
user_string = input("Please enter a string: ")

# Find the length of the string
string_length = len(user_string)

# Print the length of the string
print(f"The length of the provided string is: {string_length}")


def get_strings_lengths(str_list):
    # Get the length of each string in the list
    return [len(s) for s in str_list]

# Example usage
strings_list = ["apple", "banana", "cherry", "date


def count_the_occurrences(paragraph):
    # Convert the paragraph to lowercase to make the search case-insensitive
    paragraph = paragraph.lower()
    
    # Split the paragraph into words
    words = paragraph.split()
    
    # Count the occurrences of the word 'the'
    count = words.count('the')
    
    # Return the result
    return count

# Example usage
paragraph = input("Enter a paragraph: ")

# Count the occurrences of the word 'the'
the_count = count_the_occurrences(paragraph)

# Display the result
print(f"The word 'the' appears {the_count} times in the paragraph.")


def count_character_occurrences(input_string, character):
    # Count the occurrences of the specified character in the string
    count = input_string.count(character)
    
    # Return the result
    return count

# Example usage
input_string = input("Enter a string: ")
character = input("Enter a character to count: ")

# Count the occurrences and display the result
occurrences = count_character_occurrences(input_string, character)
print(f"The character '{character}' appears {occurrences} times in the string.")

def count_word_occurrences(text, word):
    # Convert the text to lowercase to make the search case-insensitive
    text = text.lower()
    
    # Split the text into words
    words = text.split()
    
    # Count the occurrences of the specified word
    word_count = words.count(word.lower())
    
    # Return the result
    return word_count

# Example usage
text = input("Enter the text: ")
word = input("Enter the word to count: ")

# Count the occurrences of the word
occurrences = count_word_occurrences(text, word)

# Display the result
print(f"The word '{word}' appears {occurrences} times in the text.")


def find_hello_index(input_string):
    # Find the index of the first occurrence of the word 'hello'
    index = input_string.find("hello")
    
    # Check if 'hello' is found and print the result
    if index != -1:
        print(f"The word 'hello' is found at index {index}.")
    else:
        print("The word 'hello' is not found in the string.")

# Example usage
input_string = input("Enter a string: ")
find_hello_index(input_string)



def find_character_index(input_string, character):
    # Find the index of the specified character in the string
    index = input_string.find(character)
    
    # Return the index
    return index

# Example usage
input_string = input("Enter a string: ")
character = input("Enter a character to find: ")

# Call the function and display the result
index = find_character_index(input_string, character)

if index != -1:
    print(f"The character '{character}' is found at index {index}.")
else:
    print(f"The character '{character}' is not found in the string.")


def check_if_all_lowercase(input_string):
    # Check if all characters in the string are lowercase
    if input_string.islower():
        print("All characters are lowercase.")
    else:
        print("Not all characters are lowercase.")

# Example usage
input_string = input("Enter a string: ")
check_if_all_lowercase(input_string)


def is_all_lowercase(input_string):
    # Check if the string is completely in lowercase
    return input_string.islower()

# Example usage
input_string = input("Enter a string: ")

# Check if the string is in lowercase and display the result
if is_all_lowercase(input_string):
    print("The string is completely in lowercase.")
else:
    print("The string is not completely in lowercase.")


def is_lowercase_only(input_string):
    # Check if the string contains only lowercase alphabetic characters
    if input_string.islower() and input_string.isalpha():
        print("The string contains only lowercase letters.")
    else:
        print("The string contains non-lowercase characters or non-alphabetic characters.")

# Example usage
input_string = input("Enter a string: ")

# Verify if the string is only lowercase letters
is_lowercase_only(input_string)



def is_all_uppercase(input_string):
    # Check if the string is completely in uppercase
    if input_string.isupper():
        print("The string is completely in uppercase.")
    else:
        print("The string is not completely in uppercase.")

# Example usage
input_string = input("Enter a string: ")

# Verify if the string is in uppercase
is_all_uppercase(input_string)


def check_if_uppercase(input_string):
    # Check if the string is completely in uppercase
    if input_string.isupper():
        print("The string is in uppercase.")
    else:
        print("The string is not in uppercase.")

# Example usage
input_string = input("Enter a string: ")

# Check if the string is in uppercase
check_if_uppercase(input_string)



def replace_dog_with_cat(sentence):
    # Replace all occurrences of 'dog' with 'cat'
    modified_sentence = sentence.replace("dog", "cat")
    return modified_sentence

# Example usage
sentence = input("Enter a sentence: ")

# Replace 'dog' with 'cat' and display the result
modified_sentence = replace_dog_with_cat(sentence)
print("Modified sentence:", modified_sentence)


def replace_spaces_with_underscores(input_string):
    # Replace all spaces with underscores
    modified_string = input_string.replace(" ", "_")
    return modified_string

# Example usage
input_string = input("Enter a string: ")

# Replace spaces with underscores and display the result
modified_string = replace_spaces_with_underscores(input_string)
print("Modified string:", modified_string)


def swap_case(input_string):
    # Swap the case of all characters in the string
    swapped_string = input_string.swapcase()
    return swapped_string

# Example usage
input_string = input("Enter a string: ")

# Swap the case and display the result
swapped_string = swap_case(input_string)
print("Swapped case string:", swapped_string)


def swap_case_of_sentence(sentence):
    # Swap the case of each letter in the sentence
    swapped_sentence = sentence.swapcase()
    return swapped_sentence

# Example usage
sentence = input("Enter a sentence: ")

# Get the sentence with swapped case and print the result
swapped_sentence = swap_case_of_sentence(sentence)
print("Swapped case sentence:", swapped_sentence)




































