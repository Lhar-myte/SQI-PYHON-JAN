
# def divide_two_nums():
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         result = num1 / num2
#     # except ZeroDivisionError:
#     #     print("num2 cannot be zero.")
#     #     return
#     # except ValueError:
#     #     print("num1 and num2 must be numbers")
#     #     return
#     except:
#         print("Oops! Something went wrong")   
#         return    

#     print(f"{num1}/{num2} = {result}")

# divide_two_nums()



# # Ask the user for their birth year and tell them how old they are.
# # If they enter a year less than 1 or greater than the current year, keep asking them for their
# # birth year till they enter something valid (i.e. something inbetween 1 and 2025).
# # If they enter the year as something that is not a number, keep asking them for their 
# # birth year till they enter a number.

# from datetime import datetime

# current_year = datetime.now().year


# while True:
#     try:
#         birth_year = int(input("Enter your birth year: "))
#     except ValueError as e:
#         print(f"Birth year must be a number. {e}")
#         continue

#     # if birth_year < 1 or birth_year > current_year:
#     if birth_year not in range(1, current_year + 1):
#         print("Birth year must be between 1 and 2025.")
#         continue

#     age = current_year - birth_year

#     print(f"You are {age} years old")
#     break


# class InsufficientFundsError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# class Account: 
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def format_money(self, money):
#         return "₦{:,.2f}".format(money)

#     @property
#     def formatted_balance(self):
#         return self.format_money(self.balance)

#     def __str__(self):
#         return f"""Account owner: {self.owner}
# Account balance: {self.formatted_balance}
# """    
    
#     def deposit(self, amount):
#         if amount <= 0:
#             return "Amount must be positive"
#         self.balance += amount
#         return "Deposit accepted"
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Amount must be positive"
        
#         if amount > self.balance:
#             raise InsufficientFundsError(f"Funds Unavailable. You need {self.format_money(amount - self.balance)} more to complete that transaction")
        
#         self.balance -= amount
#         return "Withdrawal accepted"
    
# acct = Account("Winifred Igboama", 70000)

# try:
#     acct.withdraw(1000000)
# except InsufficientFundsError as e:
#     print(e)

# print("End of file")

# # print("hello world"
# print(3/0)

# try:
#     name = input("Enter your name: ")
# except KeyboardInterrupt:
#     print("program terminated")


# 1. 
# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.


# class NegativeNumberError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError("Number is negative")
#     return True

# try:
#     is_positive = check_positive(float(input("Enter a number: ")))
# except NegativeNumberError as e:
#     print(e)
# else:
#     print(is_positive)
#     print("the number is positive")


# 2.
# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


# def safe_divide(a, b):
#     try:
#         result = float(a) / float(b)
#     except ZeroDivisionError:
#         return "Cannot divide by zero."
#     except TypeError:
#         return "Inputs are not numbers"
#     except ValueError:
#         return "Inputs are not convertible to floats."
#     return result

# print(safe_divide(9, "hello"))