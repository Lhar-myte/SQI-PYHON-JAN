# # Write a program that asks the user for their name and then greets them with their 
# # name: Print a greeting message that includes the user's name in the format "Hello, {name}!
# name = input("what is your name?: ")
# print(f"Hello, {name}")

# # Ask the user for their birth year and calculate their age. Print the user's age in the 
# # format “You are {age} years old.”.

# birth_year = int(input("What is year were you given birth to?: "))
# age = (2025 - birth_year)
# print(f"You are {age} years old")


# from datetime import datetime
# current_yr = datetime.now().year
# birth_year = int(input("What is year were you given birth to?: "))
# age = (current_yr - birth_year)
# print(f"You are {age} years old")

# # Ask the user for their favourite color.
# #  Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# favourite_color = input("what your favourite color?: ")
# print(f"Your favour color is {favourite_color}.")

# # Ask the user to input some text and check if it is a palindrome. 
# # A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# # Print a statement in the format “It is {is_palindrome} that {palindrome} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# text = input("write a palindrome word: ")
# reversed_text = (text[::-1])
# is_palindrome = text == reversed_text
# print(f"It is {is_palindrome} that {palindrome} is a palindrome")

# # Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# # Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# # Bonus point if you can hide the password input from displaying on the screen as clear text.

# from getpass import getpass

# password = getpass("Enter your password: ")
# is_valid = 8 <= len(password) <= 30
# print(f"It is {is_valid} that the password fulfils the criteria")

# # Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). 
# # Calculate the BMI using the formula BMI = weight / (height ** 2). 
# # Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.


height = float(input("what is your height in meters?: "))
weight = float(input("what is your weight in kilometers?: "))
bmi = (weight / (height ** 2))
bmi = (bmi , "{:.2f}".format(float(bmi)))
print(f"Your BMI is {bmi}")



plural_noun = input("Enter a plural noun: ")
last_name = input("Enter a last name of eprson in room: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a another noun: ")
part_of_the_body = input("write a part of the body: ")
part_of_the_body_2 = input("write a 2nd part of the body: ")
plural_noun_2 = input("Enter a another plural noun: ")
noun3 = input("Enter a 3rd noun: ")
noun_4 = input("Enter a 4th noun: ")
exclamation = input("Enter an exclamation: ")
noun_5 = input("Enter a 5th noun: ")
noun_6 = input("Enter a 6th noun: ")
noun_7 = input("Enter a 7th noun: ")
verb = input("Enter a verb noun: ")
noun_8 = input("Enter a 8th noun: ")
adjective_2 = input("Enter another adjective: ")
noun_9 = input("Enter a 9th noun: ")

print(f"""
A one-act play to be perform by two {plural_noun} in this room.
PATIENT: Thank you very much for seeing me Doctor {last_name}, on such {adjective1} notice.
DENTIST: What is your promble, young {noun1}?.
PATIENT: I have pain in my upper {noun2}, which is giving me a severe {part_of_the_body}ache.
DENTIST: Let me take a look. open your {part_of_the_body_2}wide, 
Good now i'm Going to tap your {plural_noun_2} with my {noun3}.
PATIENT: Shouldn't you me an {noun_4} killer?.
DENTIST: It's not neccessary yet, {exclamation}! I think i see a/an {noun_5} in your upper {noun_6}.
PATIENT: Are you going to pull my {noun_7} out?.
DENTIST: No i'm going to {verb} your tooth and put it in a temporary {noun_8}.
PATIENT: When do i come back for the {adjective_2} filling?
DENTIST: A day after i cash your {noun_9}.
""")

 