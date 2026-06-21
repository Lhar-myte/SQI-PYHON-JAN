# # 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# # statement that prints "a and b are both positive" if both a and b are positive, prints 
# # "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# # neither is positive.

# first_numbers = float(input("Enter a number?: ").strip().casefold())
# second_numbers = float(input("Enter another number?: ").strip().casefold())
# if first_numbers and second_numbers > 0:
#     print("a and b are both positive")
# elif first_numbers or second_numbers > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")

# 2, Collect three numbers x, y and z as a comma separated string input from the user and
#  print "Increasing order" if they are in STRICTLY increasing order,
#  "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x,y,z = map(int,input("Enter a three numbers? ").split(","))
# if x<y<z:
#     print("Increasing order")
# elif x>y>z:
#     print("Decreasing order")
# else:
#     print("Neither")
# 3. Write a program that reads a string called `palindrome` supplied through user input and
#  checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# palindrome = input("Enter a palindrome: ")
# if palindrome == palindrome[::-1]:
#     print("Is a palindrome")
# else:
#     print("Not a palindrome")

# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. 
# Write an if statement that checks if exactly two out of the three variables are equal and 
# prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# x = float(input("Enter a number: "))
# y = float(input("Enter second number: "))
# z = float(input("Enter third number: "))
# if x==y==z:
#     print("all same")
# elif x==y or x==z or y==z:
#     print("Two are equal")
# else:
#     print ("All different" )

# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user,
#  use if statements to check if they can form a valid triangle. Print "Valid triangle" 
# if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = float(input("Enter the first angle: "))
# angle2 = float(input("Enter the second angle: "))
# angle3 = float(input("Enter the third angle: "))
# if angle1>0 and angle2>0 and angle3>0 and (angle1 + angle2 + angle3)== 180:
#      print("Valid triangle")
# else:
#      print("Invalid triangle")
# 6. You have a single character variable `ch` supplied through user input. Write an if statement that 
# prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise.
#  Assume that the input is a single alphabet character.

# name = input("What is your name?: ").casefold().strip()
# vowels = ("a", "e", "i", "o", "u")
# if name.startswith(vowels):
#     print("Your name starts with a vowel")
# else:
#     print("Your name does not start with a vowel")

# 7. Given a comma separated string input from the user of three colors color1, color2, and color3,
#  write an if statement to check if all three colors are primary colors (red, blue, yellow).
#  Print "All primary colors" if they are, otherwise print "Not all primary colors".
# color1, color2, color3 = input("enter three colors: ").split(",")
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
# primary_colors = {"red", "blue", "yellow"}
# if {color1, color2, color3}.issubset(primary_colors):
#     print("All primary colors")
# else:
#     print("Not all primary colors")

# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". 
# Write an if statement that prints "Manual mode activated" if mode is "manuual", "Automatic mode activated" 
# if mode is "automatic", and "System is off" if mode is "off".

# mode = "automatic"
# if mode == "Automatic":
#      print("Automatic mode activated")
#  elif mode == "Manual":
#     print("Manual mode activated")
# else:
#     print("system is off")

#  9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words 
# "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". 
# Otherwise, print "Normal message".

# message = input("Enter the message: ").strip().casefold()

# high_priority_keywords = ("urgent", "important", "immediate")
# for keyword in high_priority_keywords:
#     if keyword in message:
#         print("high priority message")
#         break
# else:
#     print("Normal message")

# 10. You have two variables, status1 and status2, provided through user input, each of 
# 	which can be "active", “inactive", or "pending". Write an if statement to print 
# 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# 	and "None active" if neither is "active".

# status1 = input("write a status: ")
# status2 = input("write another status: ")
# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print("One active")
# else:
#     print("None active")

# 11.	Given a string `filename` supplied by the user, write an if statement to check if the
# 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# 	print "Not an image file".

# filename = (input("input a file name: ").casefold().strip())
# ends_with = (".jpg", ".png", ".gif")
# if filename.endswith(ends_with):
#      print("Image file")
# else:
#      print("Not an image file")

# 12. 	You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".

# access_level = input("Enter user access level: ").strip().casefold()
# if access_level == "admin":
#      print("Full access")
# elif access_level =="user":
#      print("Limited access")
#      if access_level == "guest":
#           print("No access")
# else:
#      print("No access")

# 13. Given a string `email` collected from the user, write an if statement to check if the
# 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# 	print "Invalid email".
# email = input("Enter your email: ").strip().casefold()
# if "@" in email and "." in email:
#      print("Valid email")
# else:
#      print("Invalid email")

# 14. You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# day = input("any day of the week: ").strip().casefold()
# if "saturday" in day or "sunday" in day:
#     print("weekend")
# elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
#     print("Weekday")
# else:
#     print("Invalid input")

# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	statements.
# num1, num2, num3 = input("Enter three number: ") 
# num1, num2, num3 = map(float, input("Enter three numbers separated by commas: ").split(","))
# greatest = num1
# if num2 > greatest:
#     greatest = num2
# if num3 > greatest:
#     greatest = num3
# print("The greatest number is:", greatest)

import string
alphabet = list(string.ascii_uppercase)
print(alphabet)