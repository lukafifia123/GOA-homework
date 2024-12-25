# სია
numbers = [1, 2, 3, 4, 5]

# პირველი ელემენტი
print("პირველი ელემენტი:", numbers[0])

# ბოლო ელემენტი
print("ბოლო ელემენტი:", numbers[-1])

# მეორე და მეოთხე ელემენტი
print("მეორე და მეოთხე ელემენტები:", numbers[1], numbers[3])




# სია
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

# მესამე ელემენტი
print("მესამე ელემენტი:", letters[2])

# მეორე და მეხუთე ელემენტები
print("მეორე და მეხუთე ელემენტები:", letters[1:5])

# ყოველი მესამე ელემენტი
print("ყოველი მესამე ელემენტი:", letters[::3])




# სია
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

# მესამე ელემენტი
print("მესამე ელემენტი:", letters[2])

# მეორე და მეხუთე ელემენტები
print("მეორე და მეხუთე ელემენტები:", letters[1:5])

# ყოველი მესამე ელემენტი
print("ყოველი მესამე ელემენტი:", letters[::3])





# სია
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# ბოლო ელემენტი negative indexing-ით
print("ბოლო ელემენტი:", fruits[-1])

# ბოლო სამი ელემენტი negative indexing-ით
print("ბოლო სამი ელემენტი:", fruits[-3:])




# სიის შექმნა
my_list = [10, 20, 30, 40, 50]

# პირველი ელემენტის მიღება
first_element = my_list[0]

# პირველი ელემენტის დაბეჭდვა
print(first_element)




# სიის შექმნა
my_list = [10, 20, 30, 40, 50]

# ბოლო ელემენტის მიღება negative indexing-ით
last_element = my_list[-1]

# ბოლო ელემენტის დაბეჭდვა
print(last_element)


# სიის შექმნა
my_list = [10, 20, 30, 40, 50]

# პირველი სამი ელემენტის მიღება
first_three_elements = my_list[:3]

# პირველი სამი ელემენტის დაბეჭდვა
print(first_three_elements)




# სტრიქონის შექმნა
my_string = "Hello, World!"

# ბოლო ხუთი სიმბოლოს მიღება
last_five_chars = my_string[-5:]

# ბოლო ხუთი სიმბოლოს დაბეჭდვა
print(last_five_chars)



# სტრიქონის შექმნა
my_string = "Hello, World!"

# სტრიქონის უკუღმა გადაყვანა slicing-ის დახმარებით
reversed_string = my_string[::-1]

# უკუღმა გადატრიალებული სტრიქონის დაბეჭდვა
print(reversed_string)



# სიის შექმნა
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# ყოველი მესამე ელემენტის მიღება
every_third_element = my_list[::3]

# ყოველი მესამე ელემენტის დაბეჭდვა
print(every_third_element)



# სიის შექმნა
my_list = [10, 20, 30, 40, 50, 60, 70, 80]

# სიის დაყოფა ორ ნაწილად
half_index = len(my_list) // 2  # შუა ინდექსი
first_half = my_list[:half_index]  # პირველი ნაწილი
second_half = my_list[half_index:]  # მეორე ნაწილი

# შედეგის დაბეჭდვა
print("პირველი ნაწილი:", first_half)
print("მეორე ნაწილი:", second_half)












