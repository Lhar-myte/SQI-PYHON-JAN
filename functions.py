# def greet(name):
#     print(f"Good afternoon, {name}")

# greet("Mrs. Akintola")
# greet("Mr. Adeoye")
# greet("Mr. Lekan")


# def greet_all(names):
#     greetings = []
#     for name in names:
#         greetings.append(f"Good afternoon, {name}")
#     return greetings

# greetings = greet_all(["Mrs. Akintola", "Mr. Adeoye", "Mr. Lekan"])
# for greeting in greetings:
#     print(greeting)

# def square_of_x(x):
#     return x ** 2

# result = square_of_x(5)
# print(result)

# def square_all_nums(nums):
#     print([num ** 2 for num in nums])


# print(square_all_nums([1, 2, 3, 4]))


# def add_two_nums(a, b):
#     print(a + b)


# print(add_two_nums(5, 7))

# def generate_acronym():
#     phrase = input("Enter a phrase: ").strip()
#     words = phrase.split()

#     acronym = ""

#     for word in words:
#         acronym += word[0].upper()

#         if word != words[-1]:
#             acronym += "."

#     return (acronym)

# print(generate_acronym())
# print(generate_acronym())


# Write a function called multiply that takes in two numbers a and b 
# and returns their product.


def multiply(a, b):
    return a * b

print(multiply(3, 5))

# Write a function called uppercase that takes in a string and returns the uppercase
# version of the string

# Write a function called raise_to_power that takes in base and exponent, 
# it should raise base to the power of exponent.

# Write a function called is_even that checks if a number is even or not.

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
    
# print(is_even(5))


# is_morning = False

# greeting = "Good morning" if is_morning else "Good day"

# print(greeting)


# def is_even(num):
#     return True if num % 2 == 0 else False


# def is_even(num):
#     return num % 2 == 0



# def some_func():
#     return "Some function"


# print(some_func())


# Write a function is_in_range(num, low, high) and it will return True if num is 
# inbetween low and high inclusive

def is_in_range(num, low, high):
    # return num >= low and num <= high
    # return low <= num <= high
    return num in range(low, high+1)

print(is_in_range(5, 4, 9))