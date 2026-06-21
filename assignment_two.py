# Given these;
# name = "james"  
# event = "Tech Conference"  
# date = "25th February 2025"  
# Write a program to format the invitation using string interpolation and capitalize the recipient's name.
# Print:
# "Dear James, you are cordially invited to the Tech Conference. It will be held on 25th February 2025."

name = "james"  
event = "Tech Conference"  
date = "25th February 2025"
text = "Dear {}, you are cordially invited to the {}. It will be held on {}.".format(name.capitalize(),event,date)
print(text)


# first_name = “Richie”
# Last_name = “Mighty5”

# Expected output:
# richiemighty5@gmail.com 

# NB: watch out for case senstivity. Use neccessar string methods

first_name = "Richie"
Last_name = "Mighty5"
first_name = first_name.lower()
Last_name = Last_name.lower()
email_username = first_name + Last_name + "@gmail.com"
print(email_username)


# 3. Email Validation
# From the created email address above, check; 
# a)	if the email contains "@",
# b)	 starts with their first name, 
# c)	and ends with ".com". 

# Example:
# email_address = ‘richiemighty5@gmail.com’

# Example output:
# It is [True/False] that your email contains @
# It is [True/False] that it starts with your first name, Richie.
# And it is also [True/False] it ends with .com

# NB: Use multi-line strings and the [True/False] will be the output of your string methods

email_address = "richiemighty5@gmail.com"
contains_at = "@" in email_address
starts_with_first_name = email_address.startswith(first_name)
ends_with_com = email_address.endswith(".com")
output = f"""
it is {contains_at} that your email contains @
it is {starts_with_first_name} that it starts with your first name, Richie.
and it is also {ends_with_com} that it ends with .com
"""
print(output)

# Outcode a:
# A product name (e.g., "iPhone 15")
# A launch date (e.g., "September 12, 2025")
# A standout feature (e.g., "a revolutionary AI camera")

# Then create an announcement below using string interpolation:

# Expected Output:
# "The iPhone 15 is launching on September 12, 2025, featuring a revolutionary AI camera. Get ready!"

product_name = "Iphone 15"
date = "September 12, 2025"
feature = "a revolutionary AI camera"
print(f"The {product_name} is launching on {date}, featuring {feature}. Get ready!")

# Given the sentence = "Coding is fun when coding is understood". Write a program to count how many times the word coding appears in the sentence. 
# And print;
# "The word 'coding' appears [Count] times in the sentence."
sentence = "Coding is fun when coding is understood"
print(sentence.count("coding"))

# Given the sentence = "Learning Python is exciting!" and character = "P".
# Write a program to find the first position of the character "P" in the sentence and print:
# "The first occurrence of 'P' is at index [Index]."
sentence = "Learning Python is exciting!"
character = "P"
print(sentence)










# Given the sentence = "python programming is powerful and flexible." Write a program to:
# ●	Convert the sentence to uppercase.
# ●	Convert the sentence to lowercase.
# ●	Convert the sentence to title case.
# Print all three outputs.

text = "python programming is powerful and flexible."
print(text.upper())
print(text.lower())
print(text.title())




my_tuple = ("John","peter","Vicky")
print(",".join(my_tuple))