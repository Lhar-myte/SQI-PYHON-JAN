def greet(name):
    print(f"Good afternoon, {name}")

greet("Mrs. Akintola")
greet("Mr. Adeoye")
greet("Mr. Lekan")


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


# def multiply(a, b):
#     return a * b

# print(multiply(3, 5))

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

# def is_in_range(num, low, high):
#     # return num >= low and num <= high
#     # return low <= num <= high
#     return num in range(low, high+1)

# print(is_in_range(5, 4, 9))


# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# def upper_lower(text):
#     no_of_upper = 0
#     no_of_lower = 0

#     for char in text:
#         if char.isupper():
#             no_of_upper += 1
#         elif char.islower():
#             no_of_lower += 1

#     return no_of_upper, no_of_lower

# no_of_upper, no_of_lower = upper_lower("Good Morning to You!")
# print(no_of_upper)
# print(no_of_lower)



# Write a function factorial(n) that takes in an integer n and returns the factorial of n


# def factorial(n):
#     result = 1

#     expansion = ""

#     for num in range(n, 0, -1):
#         expansion += str(num)
#         if num != 1:
#             expansion += " * "
#         result = result * num

#     return f"{n}! = {expansion} = {result}"

# print(factorial(8))


# factorial(4) => 4 * 3 * 2 * 1
# factorial(8) => 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1


# 4! = 4 * 3 * 2 * 1 = 24


# Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.



# macdonald.capitalize()
# Macdonald
# Mac + D + onald

# "mac".capitalize() => "Mac"
# "donald".capitalize() => "Donald"

# def numbers_func(numbers: list[list[int]]):
#     return numbers

# print(numbers_func([[4, 8, 9, 10], [3, 4, 5, 6, 7]]))


# def old_macdonald(name: str):
#     return name[:3].capitalize() + name[3:].capitalize()

# print(old_macdonald("macdonald"))



# def greet(time_of_day="day", name="Anonymous"):
#     return f"Good {time_of_day}, {name}"

# print(greet(name="Rebecca", time_of_day="afternoon"))
# # print(greet())

# def add_nums(single_num, *nums):

#     print(single_num)
#     print(nums)
#     total = 0
#     for num in nums:
#         total += num

#     return single_num - total

# print(add_nums(100000, 8, 9, 12, 65))

# def greet_all(*names):
#     for name in names:
#         print(f"Good afternoon, {name}")

# greet_all("Lusi", "Lekan", "Timothy", "TJ")

# type hints
# def states_and_capitals(**data: dict):
#     for key, value in data.items():
#         print(f"{key} => {value}")


# states_and_capitals(abia="Umuahia", adamawa="Yola", akwa_ibom="Uyo", anambra="Awka", oyo="Ibadan")

# data = {
#     "Abia": "Umuahia",
#     "Adamawa": "Yola",
#     "Akwa-Ibom": "Uyo",
#     "Anambra": "Awka",
#     "Oyo": "Ibadan"
# }

# states_and_capitals(**data)

# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call

# print(power(2, 100000000000000000))  # Output: 8

# 2 * power(2, 2)
# 2 * 2 * power(2, 1)
# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1 => 8

# num1 = 3
# num2 = 4



# print(num1)
# print(num2)

# def add(a: int | float, b: int | float):
#     """
#     Add two numbers and return the result.
#     a (int, float): The first number.
#     b (int, float): The second number.

#     Returns:
#     int, float: The sum of the two numbers.
#     """
#     return a + b

# print(add(1, 2))

# print(help(add))



# name = "Olamide"

# def my_func():
#     global name
#     name = "Rebecca"
#     print("Inside function: ", name)

# my_func()
# print("outside function: ", name)


# 1. Write a function called longest_word(sentence) that returns the longest word in the sentence

# def longest_word(sentence):
#     words = sentence.split()
#     longest = words[0]
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# sentence = input("Enter a sentence: ")
# print(longest_word(sentence))


# 2. Write a function to return the second largest number in a list

# def second_largest(numbers: list):
#     numbers.sort(reverse=True)
#     return numbers[1]

# print(second_largest([3, 5, 9, 1, 10]))


# def second_longest_word(sentence):
#     words = sentence.split()

#     len_words = [len(word) for word in words]

#     len_words = set(len_words)

#     len_words = list(len_words)

#     len_words.sort()

#     length_of_second_longest = len_words[-2]

#     for word in words:
#         if len(word) == length_of_second_longest:
#             return word
        
# print(second_longest_word("This is good"))

# OR

# def find_lens(word):
#     return len(word)

# def second_longest_word(sentence: str):
#     words = sentence.split()

#     words.sort(key=find_lens)

#     return words[-2]

# print(second_longest_word("The day is bright today"))