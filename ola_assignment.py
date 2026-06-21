# create a variable named `car_name` and assign the value Volvo to it.
car_name = "volvo"
# Create a variable named x and assign the value 50 to it.
x = 50
# Which of the following variable names is legal in Python?
d= "_variable3"
# Which of the following assignment statements is safe in Python?
d = "john"
# Declare variables name, age, height, and is_student, and assign them values of different types. Print the type of each variable.
name = "Lharmyte"
# Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
age = 54
height = 85
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
first_name = " John"
last_name = "Doe"
print(last_name + first_name)
# Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.
name = "Alice"
message = "Hello, {}".format(name)
print(message)

# Create a multi-line string variable using triple quotes.
text = """ 
my name is olamide,
i'm 10 years old
i live in UK
"""
print(text)

# Create a string variable word with the value "Python". Print the first and last characters using indexing.
text = "Python"
print(text[0])
print(text[5])

# Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message
word = "python"
word[2] = "r"
print(word)
# Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
x, y, z = "orange", "banana", "cherry"

# Given the string course_name = "Introduction to Python", use slicing to print: The word "Introduction".The word "Python".
course_name = "Introduction to python"
print((course_name)[0:12])
print((course_name)[16:])

# Given the string quote = "To be or not to be, that is the question.", use slicing to print:The substring "To be or not to be".The substring "that is the question".
quote ="to be or not to be, that is the question"
print((quote)[0:18])
print((quote)[20:])

# Given the string phrase = "A journey of a thousand miles begins with a single step", use slicing to print:The last 5 characters All characters except the last 7.
phrase = "a journey of a thousand miles begins with a single step"
print((phrase)[50:55])
print((phrase)[48:])
# Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
# Every second letter (A, C, E, ...).
# Every third letter starting from the first letter (A, D, G, ...).
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[0:25:2])
print(alphabet[0:25:3])
# Given the string word = "tenet", use slicing to:
# Reverse the string and print the result.
word = "tenet"
print(word[::-1])

# Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# Characters from index 9 to 19.
# Every second character from index 0 to 10.
# Every third character from the beginning to the end.
sentence = "Leaning python is fun and rewarding"
print(sentence[9:20])
print(sentence[0:11:2])
print(sentence[0::3])

# Given the string programming_language = "JavaScript", use slicing to:
# Print the first character.
# Print the last character
programming_language = "JavaScript"
print(programming_language[0:1])
print(programming_language[-1:])

# Given the string data = "DataScience", use slicing to:
# Print the substring "Science".
data = "DataScience"
print(data[4:])

# Given the string greeting = "Good Morning!", use slicing to:
# Print every second character.
greeting = "Good Morning"
print(greeting[0::2])

# Given the string name = "Alexander", use slicing to:
# Print the first three characters concatenated with the last three characters.
name = "Alexander"
print(name[0:3])+(name[6:])

