# # i = 100

# # while i >= 10:
# #     print(i)
# #     i -= 1


# # i = 0
# # while i <= 30:
# #     if i % 3 == 0:
# #         print(i)
# #     i += 1


# # i = 10.0

# # while i >= 9.0:
# #     print(round(i, 1))
# #     i -= 0.1



# # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 50


# # i = 1
# # while i <= 50:
# #     print(i, end=", ")
# #     i += 1


# # even_nos = []

# # i = 2
# # while i <= 10:
# #     if i % 2 == 0:
# #         even_nos.append(i)
# #     i += 2

# #     print(even_nos)

# # one_to_fifty = ""

# # i = 1
# # while i <= 50:
# #     # if i != 50:
# #     #     one_to_fifty = one_to_fifty + str(i) + ", "
# #     # else:
# #     #     one_to_fifty = one_to_fifty + str(i)
# #     one_to_fifty = one_to_fifty + str(i)
# #     if i != 50:
# #         one_to_fifty += ", "
# #     i += 1

# # print(one_to_fifty)

# # i = 1
# # while i <= 50:
# #     print(i, "hello", sep=",")
# #     i += 1


# # python

# # name = input("What is your name?: ")
# # i = 0

# # # while i <= len(text) - 1:
# # while i < len(name):
# #     char = name[i]
# #     print(f"The character at index {i} is {char}")
# #     i += 1

# # The character at index 0 is r
# # The character at index 1 is o
# # The character at index 2 is q

# # total = 0

# # i = 1
# # start = i
# # end = 50
# # while i <= end:
# #     total = total + i
# #     i += 1

# # print(f"The sum of numbers from {start} to {end} is {total}.")


# # 97 to 107


# # i = 97

# # while i <= 107:
# # # while i < 108:
# #     i += 1
# #     if i == 102:
# #         continue
# #     print(chr(i))


# # numbers = [0, 1, 2, 3, 4, 5, 6]

# # i = 0
# # while i < len(numbers):
# #     if i == 4:
# #         break
# #     print(numbers[i])
# #     i += 1

# # i = 0

# # shapes = ("square", "rectange", "triangle", "circle", "oval", "ellipse", "sphere")
# # while i < len(shapes):
# #     shape = shapes[i].lower()
# #     if shape.startswith("c"):
# #         break
# #     print(shape)
# #     i += 1 


# # i = 0

# # shapes = ("square", "rectange", "triangle", "circle", "oval", "ellipse", "sphere")


# # while i < len(shapes):
# #     shape = shapes[i].lower()
# #     i += 1
# #     if shape.startswith("o"):
# #         continue
# #     print(shape)

# # i = -1

# # shapes = ("square", "rectange", "triangle", "circle", "oval", "ellipse", "sphere")


# # while i < len(shapes) - 1:
# #     print(i)
# #     i += 1
# #     if shapes[i].startswith("o"):
# #         continue
# #     print(shapes[i])



# # i = 3

# # while i <= 60:
# #     i += 1
# #     if i % 2 != 0:
# #         continue

# #     if i == 50:
# #         break
# #     print(i)


# # i = 1

# # while i <= 10:
# #     print(i)
# #     if i == 100:
# #         break
# #     i += 1
# # else:
# #     print("loop has ended")


# # restaurants = ["item7", "Aroma Place", "Bite more", "Kilimanjaro", "Chicken Republic"]

# # for restaurant in restaurants:
# #     print(restaurant)


# # states_and_capitals = {"Anambra": "Awka", "Oyo": "Ibadan", "Ekiti": "Ado-Ekiti", "Ogun": "Abeokuta", "Lagos": "ikeja", "Delta": "Asaba", "Osun": "Osogbo"}

# # for state, capital in states_and_capitals.items():
# #     print(f"The capital of {state} is {capital}")



# # for num in range(97, 108):
# #     print(chr(num))
# # for num in list(range(97, 108)):
# #     print(chr(num))



# # for num in range(0, 101):
# #     if num % 3 == 0 and num % 5 == 0:
# #         print(num)


# # for num in range(0, 101, 15):
# #     print(num)


# # Write a program that simulates an ATM withdrawal process. The user should enter their 
# # balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# # not withdraw more than their balance.
# # Sample Input and Output:
# # Enter your balance: 500
# # Enter withdrawal amount: 100
# # Remaining balance: 400
# # Do you want to make another withdrawal? (yes/no): yes
# # Enter withdrawal amount: 50
# # Remaining balance: 350
# # Do you want to make another withdrawal? (yes/no): no
# # Final balance: 350


# # balance = float(input("Enter your balance: "))

# # while True:

# #     withdrawal_amt = float(input("Enter withdrawal amount: "))

# #     if withdrawal_amt > balance:
# #         print("Insufficient funds!")
# #     else:
# #         balance -= withdrawal_amt
# #         print(f"Remaining balance: {balance}")
    
# #     withdraw_again = input("Do you want to make another withdrawal? (yes/no): ").lower()

# #     if withdraw_again != "yes":
# #         print(f"Final balance: {balance}")
# #         break

# # LOOPS CORRECTION
# # 2.
# # Write a program that simulates a grocery store checkout. The user should enter the prices of items until 
# # they decide to stop. The program should calculate and display the total cost.
# # Sample Input and Output:
# # Enter item price: 2.99
# # Enter another item? (yes/no): yes
# # Enter item price: 5.49
# # Enter another item? (yes/no): no
# # Total cost: 8.48

# # total_cost = 0

# # while True:
# #     item_price = float(input("Enter item price: "))

# #     total_cost += item_price

# #     another_item = input("Enter another item? (yes/no): ").lower()
# #     if another_item != "yes":
# #         print(f"Total cost: {total_cost}")
# #         break

# # 3
# # Write a program that continuously prompts the user to enter a password until they enter a valid one.
# # A valid password must be at least 8 characters long and have a maximum of 25 characters.
# # Sample Input and Output:
# # Enter password: hello
# # Password must be at least 8 characters long and have a maximum of 25 characters.
# # Enter password: mysecretpasswordisasecret
# # Password accepted.

# # while True:
# #     password = input("Enter a password: ").strip()
# #     if 8 <= len(password) <= 25:
# #         print("Password accepted.")
# #         break
# #     else:
# #         print("Password must be at least 8 characters long and have a maximum of 25 characters.")


# # 5
# # Write a program that tracks the inventory of items in a store. The user should be able 
# # to add or remove items and the program should display the current inventory after each
# # operation. The program stops when the user decides to exit.
# # The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# # Sample Input and Output:
# # Enter operation (add/remove/exit): add
# # Enter item: eggs
# # Enter quantity: 10
# # Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# # Enter operation (add/remove/exit): remove
# # Enter item: fish
# # Enter quantity: 50
# # Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# # Enter operation (add/remove/exit): exit


# # inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}

# # while True:
# #     operation = input("Enter operation (add/remove/exit): ").lower()

# #     if operation == "exit":
# #         break

# #     if operation not in ["add", "remove"]:
# #         print("Invalid operation")
# #         continue

# #     item = input("Enter item: ")

# #     if item not in inventory:
# #         print(f"{item} not in inventory")
# #         continue

# #     quantity = int(input("Enter quantity: "))
# #     if operation == "add":
# #         inventory[item] += quantity
# #     elif operation == "remove":
# #         if quantity > inventory[item]:
# #             print(f"There are only {inventory[item]} {item} available.")
# #             continue
# #         inventory[item] -= quantity

# #     print(f"Current inventory: {inventory}")



# # inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}

# # while True:
# #     operation = input("Enter operation (add/remove/exit): ").lower()

# #     if operation == "exit":
# #         break

# #     if operation not in ["add", "remove"]:
# #         print("Invalid operation")
# #         continue

# #     item = input("Enter item: ")

# #     quantity = int(input("Enter quantity: "))
# #     if operation == "add":
# #         if item in inventory:
# #             inventory[item] += quantity
# #         else:
# #             inventory[item] = quantity

# #     elif operation == "remove":
# #         if item in inventory:
# #             if quantity > inventory[item]:
# #                 print(f"There are only {inventory[item]} {item} available.")
# #                 continue
# #             inventory[item] -= quantity
# #         else:
# #             print("That item does not exist in the inventory")
            
# #     print(f"Current inventory: {inventory}")


# # 3
# # Write a program that generates a random number between 1 and 50. Use a while loop to allow 
# # the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low.

# # from random import randint

# # attempts = 5

# # secret_num = randint(1, 50)

# # while attempts >= 1:
# #     guess = int(input("Guess the secret number: ")) 
# #     # if not(1 <= guess <= 50)
# #     if guess not in range(1, 51):
# #         print("Your guess must be between 1 and 50.")
# #         continue

# #     if guess == secret_num:
# #         print("You guessed the number correctly!")
# #         break

# #     if guess > secret_num:
# #         print("You guessed too high.")
# #     elif guess < secret_num:
# #         print("You guessed too low")

# #     attempts -= 1
# #     print(f"You have {attempts} attempts left")
# # else:
# #     print(f"You have used up all your attempts. The secret number is {secret_num}")


# # import random

# # my_list = ["apple", "avocado", "pear", "guava"]

# # random.shuffle(my_list)

# # print(my_list)

# # 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# # CORRECT_PASSWORD = "secret"

# # while True:
# #     password = input("Enter the password: ")
# #     if password == CORRECT_PASSWORD:
# #         print("Password is correct")
# #         break
# #     else:
# #         print("Incorrect")


# # 6
# # Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# # n = int(input("Enter the value of n: "))

# # i = 1
# # while i <= n:
# #     if i % 2 == 0:
# #         print(i)

# #     i += 1


# # 7
# # Write a program that takes two integers, base and exponent, from the user and uses a while loop to
# # calculate base raised to the power of exponent.
# # Sample Input:
# # Enter the base: 2
# # Enter the exponent: 3
# # Output:
# # 2 raised to the power of 3 is 8
# # Sample Input:
# # Enter the base: 5
# # Enter the exponent: 4
# # Output:
# # 5 raised to the power of 4 is 625

# # base = int(input("Enter the base: "))
# # exponent = int(input("Enter the exponent: "))

# # i = exponent

# # result = 1
# # while i >= 1:
# #     result *= base
# #     i -= 1

# # print(f"{base} raised to the power of {exponent} is {result}")


# # base = int(input("Enter the base: "))
# # exponent = int(input("Enter the exponent: "))

# # i = 0

# # result = 1
# # while i < exponent:
# #     result *= base
# #     i += 1

# # print(f"{base} raised to the power of {exponent} is {result}")


# # Write a program that takes a string input from the user and uses a while loop to 
# # count the number of vowels (a, e, i, o, u) in the string.

# # hello
# # 2

# # text = input("Enter some text: ").lower().strip()
# # vowels = "aeiou"

# # i = 0
# # no_of_vowels = 0
# # while i < len(text):
# #     char = text[i]
# #     if char in vowels:
# #         no_of_vowels += 1
# #     i += 1

# # print(f'There are {no_of_vowels} vowels in "{text}"')


# # 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.

# # text = input("Enter some text: ")

# # reversed_text = ""

# # i = len(text) - 1
# # while i >= 0:
# #     char = text[i]
# #     reversed_text += char
# #     i -= 1

# # print(reversed_text)


# # 10. Write a program that takes comma-separated integers from the user, converts that
# # to a tuple and uses a while loop to find the minimum value in the tuple.

# # numbers = tuple(input("Enter integers separated by commas e.g. 7, 2, 4: ").strip().split(","))

# # min_num = int(numbers[0])

# # i = 1

# # while i < len(numbers):
# #     num = int(numbers[i])

# #     print("current number: ", num)

# #     print("current minimum number: ", min_num)

# #     if num < min_num:
# #         min_num = num
# #     i += 1

# # print(f"The minimum number is {min_num}")

    

# # 11. Write a program that takes a string input from the user and uses a while loop to count
# # the occurrences of each character, storing the counts in a dictionary.
# # Sample Input:
# # Enter a string: Hello
# # Sample Output:
# # {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}



# # text = input("Enter some text: ")

# # occurences = {}

# # i = 0

# # while i < len(text):
# #     char = text[i]
# #     if char in occurences:
# #         occurences[char] += 1
# #     else:
# #         occurences[char] = 1
# #     i += 1

# # print(occurences)


# # Write a program that takes a string input from the user and uses a while loop to count
# # the occurrences of uppercase and lowercase letters, storing the counts in a dictionary.
# # Sample Input:
# # Enter a string: GOOD day, I AM hAppy
# # Sample Output:
# # {"uppercase": 8, lowercase: 7}

# # occurences = {"uppercase": 0, "lowercase": 0}

# # text = input("Enter some text: ")

# # i = 0
# # while i < len(text):
# #     char = text[i]

# #     if char.isupper():
# #         occurences["uppercase"] += 1
# #     elif char.islower():
# #         occurences["lowercase"] += 1

# #     i += 1


# # print(occurences)




# # Create a list called `steps` containing "start", "process", "skip", and "finish".
# # Loop through the list using a for loop but skip the "skip" step
# # Your output should have start, process, finish


# # steps = ["start", "process", "skip", "finish"]

# # for step in steps:
# #     if step == "skip":
# #         continue
# #     print(step)



# # steps = ["start", "process", "skip", "stop", "finish"]
# # # Loop through the steps, stop once you reach stop, BUT MAKE SURE stop IS PRINTED TOO
# # # This means you should not print "finish"

# # for step in steps:
# #     print(step)
# #     if step == "stop":
# #         break


# # for num in range(4, 20, 3):
# #     print(num)



# # text = "akin"
# # for idx, char in enumerate(text, start=1):
# #     print(f"The character at position {idx} is {char}")


# # import string
# # alphabets = string.ascii_lowercase



# # text = "akin"
# # for char in text:
# #     for idx, alphabet in enumerate(alphabets, start=1):
# #         if char == alphabet:
# #             print(f"{char} is at position {idx}")
# #             break


# # animes = ["AOT", "Naruto", "Demon Slayer", "One Piece", "Death Note"]

# # 1. AOT
# # 2. Naruto
# # 3. Demon Slayer
# # 4. One Piece
# # 5. Death Note

# # for idx, anime in enumerate(animes, start=1):
# #     print(f"{idx}. {anime}")
# #     if anime == "One Piece":
# #         break
# # else:
# #     print("end of numbered list")


# # adjectives = ["fierce", "majestic", "playful"]
# # animals = ["lion", "eagle", "dolphin"]

# # for adjective in adjectives:
# #     for animal in animals:
# #         if adjective == "playful" and animal == "lion":
# #             continue
# #         print(f"{adjective} {animal}")


# # adjectives = ["fierce", "majestic", "playful"]
# # animals = ["lion", "eagle", "dolphin"]

# # i = 0
# # while i < len(adjectives):
# #     print(f"{adjectives[i]} {animals[i]}")
# #     i += 1

# # for adjective, animal in zip(adjectives, animals):
# #     print(f"{adjective} {animal}")

# # animals = ["lion", "eagle", "dolphin"]
# # for animal in animals:
# #     # print(animal)
# #     pass



# animals = ["lion", "eagle", "dolphin"]
# # animals_copy = animals.copy()

# # animals.append("goat")

# # print(animals)
# # print(animals_copy)

# # animals = ["lion", "eagle", "dolphin"]

# # animals_copy = []

# # for animal in animals:
# #     animals_copy.append(animal)

# # animals_copy = [animal for animal in animals]


# # print(animals)
# # print(animals_copy)


# # tv_shows = ["Westworld", "GOT", "Night Agent", "The Big Bang Theory", "Young Sheldon", "House of the Dragon"]

# # tv_shows_copy = [tv_show for tv_show in tv_shows]
# # print(tv_shows_copy)

# # tv_shows_copy.append("Day of the Jackal")

# # print(tv_shows_copy)



# # numbers = [6, 7, 100, 1, 4, 78]

# # even_nos = []

# # for num in numbers:
# #     if num % 2 == 0:
# #         even_nos.append(num)

# # print(even_nos)


# # numbers = [6, 7, 100, 1, 4, 78]

# # is_even = [True, False, True, False, True, True]

# # even_nos = [num for num in numbers if num % 2 == 0]
# # print(even_nos)

# # is_even = [num % 2 == 0 for num in numbers]
# # print(is_even)



# # players = ("Ronaldo", "Messi", "Aguero", "Sane", "Mane", "Hazard", "Halland", "Rashford", "Griezmann")

# # # players_that_start_with_m = [player for player in players if player.startswith("M")]
# # players_that_start_with_m = [player for player in players if player[0] == "M"]

# # players_that_start_with_m = [player.startswith("M") for player in players]

# # players_that_start_with_m = [player[0] == "M" for player in players]

# # print(players_that_start_with_m)


# # even_nos_up_to_50 = [num for num in range(0, 51) if num % 2 == 0]
# # odd_nos_up_to_50 = [num for num in range(0, 51) if num % 2 != 0]

# # print(even_nos_up_to_50)
# # print(odd_nos_up_to_50)


# # 10 => 1, 2, 5, 10
# # 20 => 1, 2, 4, 5, 10, 20

# # factors_of_50 = [num for num in range(1, 51) if 50 % num == 0]


# # print(factors_of_50)


# # numbers = [78, 20, 21, 67, 100]

# # create a variable numbers_less_than_60 that will contain all the numbers 
# # that are less than 60 in numbers

# # numbers_less_than_60 = any(num < 60 for num in numbers)

# # print(numbers_less_than_60)


# # players = ("Ronaldo", "Messi", "Aguero", "Sane", "Mane", "Hazard", "Halland", "Rashford", "Griezmann")

# # players_upper = [player.upper() for player in players]
# # print(players_upper)

# # len_players = {player: len(player) for player in players}
# # print(len_players)



# # factors_of_50 = (num for num in range(1, 51) if 50 % num == 0)

# # print(list(factors_of_50))


# # Check if all the strings start with a vowel

# # languages = ("Python", "Java", "Angular", "C++", "Go", "Elixir")

# # vowels = ("a", "e", "i", "o", "u")

# # all_start_with_vowels = [lang.lower().startswith(vowels) for lang in languages]
# # all_start_with_vowels = all([lang[0].lower() in vowels for lang in languages])


# print(all_start_with_vowels)

# from getpass import getpass

# password = getpass("Enter your password: ").strip()
# password = "Password123)"

# special_chars = "&^%#@!()+-._"

# has_uppercase = any(char.isupper() for char in password)

# has_lowercase = any(char.islower() for char in password)

# digits = range(0, 10)
# # str_digits = [str(digit) for digit in digits]

# # has_digit = any(char in str_digits for char in password)
# # print(has_digit)

# # has_digit = any(char.isdigit() for char in password)

# # has_special_char = any(char in special_chars for char in password)

# # print(has_uppercase and has_lowercase and has_special_char)


# # table = int(input("Enter the multiplication table: "))

# # for num in range(0, 13):
# #     print(f"{table} X {num} = {table*num}")

# # 5 X 1 = 5
# # 5 X 2 = 10
# # ...
# # 5 X 12 = 60

# # inp = int(input("Enter a number: "))

# # for num in range(1, 13):
# #     result = inp * num
# #     print(f"{inp} X {num} = {result}")
    








