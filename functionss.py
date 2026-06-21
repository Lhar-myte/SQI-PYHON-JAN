# # def multiply(a,b):
# #     return(a*b)
# # print(multiply(1,2))

# # def uppercase(num):
# #     return text.upper()

# # text = input("Enter a text: ")
# # print(uppercase(text))

# # def cube(num):
# #     return num**3
# # # num = int(input("Enter a number: "))
# # print(cube(4))

# # def raised_to_power(base, exponent):
# #     return base ** exponent
# # print(raised_to_power(3, 4))

# # def is_even(num):
# #     if num % 2==0:
# #         return True
# #     else:
# #         return False
# # print(is_even(5))

# # def is_in_range(num, low, high):
# #     return num >= low and num <= high
# # print(is_in_range(12, 4, 9))
# # def factorial(n):
# #     result = 1
# #     for i in range(1, n+1):
# #         result *= i
# #     return result
# # print(factorial(int(input("Enter the valu ef n: "))))
# # first_part =""
# # second_part =""
# # third_part =""
# # def old_macdonald (name):
# #     first_part = name[0:3].capitalize()
# #     second_part = name [3].title()
# #     third_part = name [4:]
# #     return first_part + second_part + third_part
# # print( old_macdonald("macdonald"))
 






# # def longest_word(sentence):
# #     word = sentence.split()
# #     longest = word[0]
# #     for sentence in sentence:
# #         if len(word) > len(longest):
# #             longest = word
# #     return longest

# # print(longest_word(input("Enter a sentence: ")))


# def second_largest_number(numbers):
#     numbers.sort(reverse=True)
#     return numbers[1]
# print(second_largest_number([8,9,7]))



# Write a function is_even(n) that returns True if n is even and False if n is odd.

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(4))


# Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, 
# # but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     if a % 2 != 0 or b % 2 != 0:
#         return max(a, b)
# print(lesser_of_two_evens(2, 2))

# Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(list_of_ints):
#     code = [0,0,7]
#     for num in list_of_ints:
#         if num == code[0]:
#             code.pop(0)
#         if not code:
#             return True
#     return False
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True 
# if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

def is_alliteration(two_word_string):
    word = two_word_string.split()
    if word[[0][0]] == word[[1][0]]:
            return True
    else:
        return False
print(is_alliteration("Levelheaded Llama"))


    

# def area_of_circle(radius, pi=22/7):
#     return  (pi * radius ** 2)
# print(area_of_circle(40,))
