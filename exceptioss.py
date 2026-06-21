# # from datetime import datetime
# # while True:
# #     current_year = datetime.now().year
# #     try:
# #         birth_year = int(input("Enter your birth year: "))
# #     age = current_year - birth_year 
# #     print(f"you are {age} years old")
# #     if birth_year >= 1 or birth_year <= current_year:
# #     print("birth year must be more than 1 and not the same as the current year")
# # except 



# # 1. Define a custom exception called NegativeNumberError.
# # Write a function check_positive(number) that raises 
# # NegativeNumberError if the input number is negative.
# # Catch the exception when calling the function.

class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
       raise NegativeNumberError(F"number must be positive")
    else:
        return "positive number"
while True:   
    try:    
        print(check_positive( int(input("Enter a nuber: "))))
        break
    except NegativeNumberError as e:
        print(e)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        break
    
    


# # 2. Handle Multiple Exceptions:
# # Write a function safe_divide(a, b) that performs division.
# # Handle ZeroDivisionError if the divisor is zero.
# # Handle TypeError if the inputs are not numbers.
# # Handle ValueError if the inputs are not convertible to floats.

def safe_divide():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a / b
        print(f"{a}/{b} = {result}")

    except ZeroDivisionError:
        print("number assigned to 'b' must be more than 0")
        return
    except TypeError:
        print("number assigned to 'a' and 'b' must be more an integer")
        return

    except ValueError:
        print("number assigned to 'a' and 'b' must be input convertible to a float")
        return
    

safe_divide()