def welcome_message(name, age):
    # Using an f-string to format the message
    return f"Hello, {name}! You are {age} years old. Welcome!"

# Example usage:
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

# Convert age to integer
user_age = int(user_age)

message = welcome_message(user_name, user_age)
print(message)



def format_name(first_name, last_name):
    # Capitalize both first and last name, then combine them into a single string
    full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
    return full_name

# Example usage:
first = input("Enter your first name: ")
last = input("Enter your last name: ")

formatted_name = format_name(first, last)
print(f"Formatted Name: {formatted_name}")


def reverse_and_format(string):
    # Reverse the string and format it into a sentence
    reversed_string = string[::-1]
    return f"The reversed string is: {reversed_string}"

# Example usage:
input_string = input("Enter a string: ")

formatted_sentence = reverse_and_format(input_string)
print(formatted_sentence)


def insert_word(sentence, word, index):
    # Split the sentence into words, insert the new word, and join them back into a sentence
    sentence_words = sentence.split()
    
    # Insert the word at the specified index
    sentence_words.insert(index, word)
    
    # Join the list of words back into a sentence and return it
    return ' '.join(sentence_words)

# Example usage:
sentence = input("Enter a sentence: ")
word = input("Enter a word to insert: ")
index = int(input("Enter the index at which to insert the word: "))

new_sentence = insert_word(sentence, word, index)
print(f"New sentence: {new_sentence}")


def sentence_to_words(sentence):
    # Split the sentence into a list of words using split()
    words = sentence.split()
    return words

# Example usage:
sentence = input("Enter a sentence: ")

words_list = sentence_to_words(sentence)
print(f"List of words: {words_list}")


def csv_to_list(csv_string):
    # Split the string at commas and return a list of items
    items = csv_string.split(',')
    return items

# Example usage:
csv_input = input("Enter a CSV string: ")

items_list = csv_to_list(csv_input)
print(f"List of items: {items_list}")


def split_into_sentences(paragraph):
    # Split the paragraph into sentences based on periods
    sentences = paragraph.split('.')
    
    # Remove any leading or trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence]
    
    return sentences

# Example usage:
paragraph = input("Enter a paragraph: ")

sentences_list = split_into_sentences(paragraph)
print(f"List of sentences: {sentences_list}")


def append_item_to_list(my_list, item):
    # Append the item to the list
    my_list.append(item)
    return my_list

# Example usage:
my_list = [1, 2, 3]
item = input("Enter an item to append: ")

# Append the item to the list
updated_list = append_item_to_list(my_list, item)
print(f"Updated list: {updated_list}")



def append_items_to_list(original_list, items_list):
    # Append each item from items_list to the original_list
    original_list.extend(items_list)
    return original_list

# Example usage:
original_list = [1, 2, 3]
items_list = [4, 5, 6]

# Append the items to the original list
updated_list = append_items_to_list(original_list, items_list)
print(f"Updated list: {updated_list}")



def append_all_elements(list1, list2):
    # Append all elements of list2 to list1
    list1.extend(list2)
    return list1

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append all elements of list2 to list1
updated_list = append_all_elements(list1, list2)
print(f"Updated list: {updated_list}")


def insert_item_at_index(my_list, index, item):
    # Insert the item at the specified index in the list
    my_list.insert(index, item)
    return my_list

# Example usage:
my_list = [1, 2, 3, 4]
index = int(input("Enter the index where you want to insert the item: "))
item = input("Enter the item to insert: ")

# Insert the item at the specified index
updated_list = insert_item_at_index(my_list, index, item)
print(f"Updated list: {updated_list}")

def insert_item_at_beginning(my_list, item):
    # Insert the item at the beginning of the list
    my_list.insert(0, item)
    return my_list

# Example usage:
my_list = [2, 3, 4]
item = input("Enter the item to insert at the beginning: ")

# Insert the item at the beginning of the list
updated_list = insert_item_at_beginning(my_list, item)
print(f"Updated list: {updated_list}")


def insert_item_at_end(my_list, item):
    # Insert the item at the end of the list using the insert method
    my_list.insert(len(my_list), item)
    return my_list

# Example usage:
my_list = [1, 2, 3]
item = input("Enter the item to insert at the end: ")

# Insert the item at the end of the list
updated_list = insert_item_at_end(my_list, item)
print(f"Updated list: {updated_list}")





