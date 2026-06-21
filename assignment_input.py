# # 1. Password Validation
# # Task: Write a program that asks the user to enter a password and confirm it. 
# # Use comparison operation to check if the two inputs match and the results should print either True or False

# from getpass import getpass
# password = getpass("Enter your password: ")
# print(password)

# confirm_password = getpass("Enter a confirm password: ")
# print(confirm_password)

# print(password == confirm_password)

# # 2. Age in 10 Years
# # Task: Ask the user for their age and calculate what their age will be in 10 years.
# # (Hint: Use type conversion for the arithmetic.)

calculate_age_in_10_years():
current_age = int(input("Enter your current age: "))
age_in_10_years = current_age + 10
print("your age in 10 years will be:", age_in_10_years)





# # Task: Ask the user to input their full name (first, middle, last). Extract and print the initials in uppercase.
# # Example Input (on terminal):
# # 		>>> What is your full name? John Michael Smith
# # Output:
# # 		Your initials are J.M.S.
# full_name = input("What is your full name?")
# names = full_name.split()
# initials = [name[0].upper() for name in names]
# print("your initials are:", ".".join(initials))


# # Task: Ask the user to enter their first name and last name. Print their name in reverse order: Last Name, First Name.
# # Example Input:
# # 		>>> What is your name? Emily Brown
# # Output:
# # 		Your name in reverse order is Brown, Emily.

full_name = input("what is your full name?")
names = full_name.split()
reversed_name = ", ".join(reversed(names))
print("your name in reversed order:", reversed_name)


# # Task: Ask the user to input a sentence. Split the sentence into words and join them back together with a hyphen (-) as a separator.
# # Example Input:
# # 		Enter a sentence: Python is fun!
# # Output:
# # 		Hyphenated sentence: Python-is-fun!
# sentence = input("Enter a sentece: ")
# words = sentence.split()
# hyphenated_sentence = "-".join(words)
# print("Hyphanated sentence:", hyphenated_sentence)



alphabet = input("write a vowel alphabet: ")
vowel = "aeiou"
print(f"It is {alphabet in vowel} that {alphabet} is a vowel")