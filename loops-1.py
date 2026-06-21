# i = 100

# while i >= 10:
#     print(i)
#     i -= 1


# i = 0
# while i <= 30:
#     if i % 3 == 0:
#         print(i)
#     i += 1


# i = 10.0

# while i >= 9.0:
#     print(round(i, 1))
#     i -= 0.1



# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 50


# i = 1
# while i <= 50:
#     print(i, end=", ")
#     i += 1


# even_nos = []

# i = 2
# while i <= 10:
#     if i % 2 == 0:
#         even_nos.append(i)
#     i += 2

#     print(even_nos)

# one_to_fifty = ""

# i = 1
# while i <= 50:
#     # if i != 50:
#     #     one_to_fifty = one_to_fifty + str(i) + ", "
#     # else:
#     #     one_to_fifty = one_to_fifty + str(i)
#     one_to_fifty = one_to_fifty + str(i)
#     if i != 50:
#         one_to_fifty += ", "
#     i += 1

# print(one_to_fifty)

# i = 1
# while i <= 50:
#     print(i, "hello", sep=",")
#     i += 1


# python

# name = input("What is your name?: ")
# i = 0

# # while i <= len(text) - 1:
# while i < len(name):
#     char = name[i]
#     print(f"The character at index {i} is {char}")
#     i += 1

# The character at index 0 is r
# The character at index 1 is o
# The character at index 2 is q

# total = 0

# i = 1
# start = i
# end = 50
# while i <= end:
#     total = total + i
#     i += 1

# print(f"The sum of numbers from {start} to {end} is {total}.")


# 97 to 107


# i = 97

# while i <= 107:
# # while i < 108:
#     i += 1
#     if i == 102:
#         continue
#     print(chr(i))


# numbers = [0, 1, 2, 3, 4, 5, 6]

# i = 0
# while i < len(numbers):
#     if i == 4:
#         break
#     print(numbers[i])
#     i += 1

# i = 0

# shapes = ("square", "rectange", "triangle", "circle", "oval", "ellipse", "sphere")
# while i < len(shapes):
#     shape = shapes[i].lower()
#     if shape.startswith("c"):
#         break
#     print(shape)
#     i += 1 


# i = 0

# shapes = ("square", "rectange", "triangle", "circle", "oval", "ellipse", "sphere")


# while i < len(shapes):
#     shape = shapes[i].lower()
#     i += 1
#     if shape.startswith("o"):
#         continue
#     print(shape)

# i = -1

# shapes = ("square", "rectange", "triangle", "circle", "oval", "ellipse", "sphere")


# while i < len(shapes) - 1:
#     print(i)
#     i += 1
#     if shapes[i].startswith("o"):
#         continue
#     print(shapes[i])



# i = 3

# while i <= 60:
#     i += 1
#     if i % 2 != 0:
#         continue

#     if i == 50:
#         break
#     print(i)


# i = 1

# while i <= 10:
#     print(i)
#     if i == 100:
#         break
#     i += 1
# else:
#     print("loop has ended")


# restaurants = ["item7", "Aroma Place", "Bite more", "Kilimanjaro", "Chicken Republic"]

# for restaurant in restaurants:
#     print(restaurant)


# states_and_capitals = {"Anambra": "Awka", "Oyo": "Ibadan", "Ekiti": "Ado-Ekiti", "Ogun": "Abeokuta", "Lagos": "ikeja", "Delta": "Asaba", "Osun": "Osogbo"}

# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")



# for num in range(97, 108):
#     print(chr(num))
# for num in list(range(97, 108)):
#     print(chr(num))



# for num in range(0, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)


# for num in range(0, 101, 15):
#     print(num)


# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350


balance = float(input("Enter your balance: "))

while True:

    withdrawal_amt = float(input("Enter withdrawal amount: "))

    if withdrawal_amt > balance:
        print("Insufficient funds!")
    else:
        balance -= withdrawal_amt
        print(f"Remaining balance: {balance}")
    
    withdraw_again = input("Do you want to make another withdrawal? (yes/no): ").lower()

    if withdraw_again != "yes":
        print(f"Final balance: {balance}")
        break