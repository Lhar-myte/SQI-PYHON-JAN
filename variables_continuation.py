# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"

# Instructions:
# Extract and preprocess the components:
# Author: Capitalize the first letter of the author's names i.e. title case
# Book Title: Trim any leading and trailing whitespaces and convert the title to be in title case.
# ISBN Number: Correct the typo in the ISBN number by replacing ISN with ISBN.
# Cost: Format the cost to 2 decimal places and prepend the naira symbol ₦.
# Format the information into a new multi-line string called `formatted_book_info` using an f-string or the format method.
# The output should be of the format:
# The book `book_title` was written by `author` and published in `year_published`.
# It has `no_of_pages` pages and `isbn` and costs `cost`.
# Using the example above, the expected output is: 


# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"

# details_list = book_info.split(" ; ")
# print(details_list)

# arthor = details_list[0].title()
# book_title = details_list[1].title()
# year = details_list[2]
# isbn_no = details_list[3].replace("ISN", "ISBN")
# pages = details_list[4]
# cost = f"#{details_list[5]}.00"

# print(
# f"""The book {book_title} was written by {arthor} and published in {year}.
# It has {pages} pages and {isbn_no} and costs {cost}.
# """)



# price = 50000000
# price2 = 5e7

# print(price)
# print(price2)

# print(45/3)

# num1 = int(input("Enter your age;"))
# print(num1)

# print(type(num1))
# print(type(int(num1)))


x = 6
y = 4
y += 23
print(y)

# print( type(x == y ))

# price = 67.00
# age = 60

# print(age > price)
# print(age != price)
# print(age >= price)

# name = True
# print(bool(name))

# my_dict = {"name" : "Richard", "age" : 55 }
# print(my_dict.items())

# name = 'Richard', 'Olamide'
# print(type(name))


# first_name = name[0]

# first_name, second_name = name
# print(first_name, first_name)
# print(second_name)




# x = y = z = 5
# print(x)
# print(y)
# print(z)




# Create two string variables: first_name with value "John" and last_name with value 
# "Smith". Concatenate them together with a space in between and print the result.

first_name ='John'
last_name = 'Smith'
print(first_name + " " + last_name)


# Given the string word = "Python", print the first character.
word = "Python"
print(word[0])


# Create a string variable greeting with the value "Hello". Use string interpolation to insert the name "Alice"
#  into the greeting and print the result.
text = "Hello"
print(f"{text}, Alice")


# Given the strings part1 = "Data" and part2 = "Science", concatenate them to form "DataScience" and print the result.



# Given the string phrase = "Welcome", print the last character using negative indexing.

# Create a string variable food with the value "pizza". Use string interpolation to create the sentence "I love pizza" and print it.
# Given the strings str_1 = "Good" and str_2 = "Morning", concatenate them with a space in between to form "Good Morning" and print the result.
# Given the string text = "Concatenate", print the character at index 5.
# Create a variable age with the value 25. Use string interpolation to create the sentence "I am 25 years old" and print it.
# Create three string variables: city = "New", space = " ", and country = "York". Concatenate them to form "New York" and print the result.