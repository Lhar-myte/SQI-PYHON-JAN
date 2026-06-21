# i = 49
# while 30 < i:
#     print(i)
#     i -= 2

# i = 2
# while i <= 20:
#     print(i)
#     i += 2

# i = 10.0
# while 9.0 <= i:
#     print(round(i, 1))
#     i -= 0.1

# i = 0
# while 30 >= i:
#     if i % 3 == 0:
#      print(i)
#     i += 1

# numbers = ""
# i = 1
# while 50 >= i:
#     if i != 50:
#         numbers = numbers + str(i) + "," 
#     else: 
#         numbers = numbers + str(i)
#     i += 1   
# print(numbers)

# name = input("Enter your name: ")
# i = 0
# while i < len(name):
#     char = name[i]
#     print("the character at index",(i),"is", char)
#     i += 1

# num_total = 0
# i = 0
# while i <= 50:
#     num_total = num_total + i 
#     i += 1
# print(num_total)


# i = 97
# while i <= 107:
#     print(chr(i))
#     i += 1

shapes = ("square","rectangle", "triangle", "circle", "oval", "ellipse", "sphere")
# i = -1
# while i < len(shapes) -1:
#     i += 1
#     if shapes[i].startswith("o"):
#         continue
#     print(shapes[i])
# i = 0
# while i < len(shapes):
#     shape = shapes[i].lower()
#     i += 1
#     if shape.startswith("o"):
#         continue
#     print(shape)

# front_row = ("timothy", "olamide", "rebecca", "heritage", "lusi", "Mrs akintola", "roqeeb")
# for name in front_row:
#     print(name)

# numbers = list(range(0, 101,15))
# for num in numbers:
#     print(num)

# # numbers = list(rang 

# steps = ("steps", "containg", "process", "skip","stop", "finish")
# # for step in steps:
# #     if step == "skip":
# #         continue
# #     print(step)

# for step in steps:
#     print(step)
#     if step == "stop":
#         break

# animes = ["ADT", "Naruto", "Demon Slayer", "One piece", "Death Note"]
# for idx,anime in enumerate(animes, start=1):
#     print(f"{idx}. {anime}")

# football_players = ("Ronaldo","Messi","Aguero","Sane","Mane","Hazard","Halland","Rashford","Greizeman")
# # football_players_startwith_m =[football_player for football_player in football_players if football_player.startswith("M")]
# # print(football_players_startwith_m)
 
# football_players_startwith_m =[football_player for football_player in football_players if football_player[] =="M" ]
# print(football_players_startwith_m)

# numbers = [78, 20, 21, 67, 100]
# less_than_60 = [num for num in numbers if num < 60]
# print(less_than_60)

# less_than_60 = [num < 60 for num in numbers ]
# print(less_than_60)

# football_players = ("Ronaldo","Messi","Aguero","Sane","Mane","Hazard","Halland","Rashford","Greizeman")
# football_players_capital = [football_player.upper() for football_player in football_players ]
# print(football_players_capital)

# players = ("Ronaldo","Messi","Aguero","Sane","Mane","Hazard","Halland","Rashford","Greizeman")
# char_players = {player: player.lower().count("a") for player in players}
# # print(char_players)

# languages = ("Python", "Java", "C++", "Go", "Elixer")
# vowel = ("a","e","i,","o","u")
# startwith_vowel = [language.lower().startswith(vowel) for language in languages]
# print(startwith_vowel)


# startwith_vowel = all(language.lower().startswith(vowel) for language in languages)
# print(startwith_vowel)


# table = int(input("Enter the multiplication table: "))
# for num in range(0,13):
#     print(f"{table} X {num} = {table * num}")




# 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)
# # Take input from the user

# # num = input("Enter an integer: ")
# # sum_digits = 0
# # for digit in num:
# #     sum_digits += int(digit)  
# # print("Sum of digits:", sum_digits)

# # 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string.
# #  Print the counts. Example:
# # Input: "hello world"
# # Output: Vowels: 3, Consonants: 7
# alphabets = input("Enter an alphabet: ")
# vowels = "a","e","i","o","u"
# vowel_count = 0
# consonant_count = 0
# for char in alphabets:
#     if char.isalpha():  # Check if character is a letter
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print(f"vowels:{vowel_count}, consonants:{consonant_count}")    

# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any
#  duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# numbers = (input("Enter numbers seperated by commas: "))
# num_list = [int(num) for num in numbers.split(",")]
# new_list =[]
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

# 7. Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# numbers = (input("Enter numbers seperated by commas: "))
# num_list = [int(num) for num in numbers.split(",")]
# largest = num_list[0]
# for num in num_list:
#     if num > largest:
#         largest = num
# print(largest)

# 8. Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# n = int(input("Enter an integer: "))
# sum_even_num = 0
# for i in range(2, n + 1, 2):
#     sum_even_num += i
# print(sum_even_num)
    
# 10. Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input("Enter an integer: "))
# sum_of_squares = 0
# for i in range(1, n + 1,):
#     sum_of_squares += i ** 2
# print(sum_of_squares)

# 11. Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

# text = input("Enter a text: ")
# words = text.split()
# acronmy = ""
# for char in words:
#     acronmy += char.upper()[0]
# print(acronmy)

# 12. Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

# text = input("Enter a text: ")
# words = text.split()
# text_count = 0
# for word in words:
#     text_count += 1
# print(text_count)

# 13. Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

# text = input("Enter a text: ")
# words = text.lower().split()
# letters_startwith_s = [word for word in words if word.startswith("s")]
# print(letters_startwith_s)
# for word in letters_startwith_s:
#     print(word)

# 15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.

for num in range(1,51):
    if num % 3 == 0:
        print(num)