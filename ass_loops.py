# #  1.Write a program that uses a while loop to print numbers from 1 to 10.
# # i = 1
# # while i <= 10:
# #     print(i)
# #     i += 1

# # # 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`
# # correct_password = "secret"
# # while True:
# #     password = input("Enter your pass word: ").lower().strip()
# #     if password == correct_password:
# #         print("Access granted")
# #         break
# #     else:
# #         print("incorrect password")

# # 5. Write a program that takes an integer input from the user and uses a while loop to print a countdown 
# # from that number to zero.

# # user = int(input("write an integer: "))
# # # i = 0
# # while 0 <= user:
# #     print(user)
# #     user -= 1


# # # 6. Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# # user = int(input("write an integer: "))
# # i = 1
# # while i <= user:
# #     if i % 2 == 0:
# #      print(i)
# #     i+=1

# # 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to 
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

# # numb1 = int(input("Enter the base: "))
# # numb2 = int(input("Enter the exponent: "))
# # i = numb2

# # output = 1
# # while i >= 1:
# #     output *= numb2  
# #     i -= 1
# # print(f"{numb1} raised to the power of {numb2} is {output}" )

# # part 2
# # 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until 
# # they decide to stop. The program should calculate and display the total cost.
# # Sample Input and Output:
# # Enter item price: 2.99
# # Enter another item? (yes/no): yes
# # Enter item price: 5.49
# # Enter another item? (yes/no): no
# # Total cost: 8.48

# # total_cost = 0
# # while True:
# #     price_grocery_items = float(input("Enter item price: "))
# #     total_cost += price_grocery_items
# #     grocery_items2 = (input("Enter another item? (yes/no) "))
# #     if grocery_items2 != "yes":
# #         print(f"Total cost: {total_cost}")
# #         break
    
# # 3.Write a program that continuously prompts the user to enter a password until they enter a valid one. 
# # A valid password must be at least 8 characters long and have a maximum of 25 characters.
# # Sample Input and Output:
# # Enter password: hello
# # Password must be at least 8 characters long and have a maximum of 25 characters.
# # Enter password: mysecretpasswordisasecret123
# # Password accepted.

# # while True:
# #     password = input("Enter your password: ")
# #     if 8 <= len(password) <= 25:
# #         print("Password accepted")
# #         break
# #     else: 
# #         print("Password must be at least 8 characters long and have a maximum of 25 characters")

# # 4. Write a program that asks for the user's age and keeps prompting them until they 
# # 	enter a valid age (greater than or equal to 0).
# # 	Sample Input and Output:
# # 	Enter your age: -5
# # 	Invalid age. Please enter a valid age.
# # 	Enter your age: 25
# # 	Age accepted.
# # while True:
# #     age = int(input("Enter your age: "))
# #     if age >= 0:
# #         print("Age accepted")
# #         break
# #     else:
# #         print("Invalid age. Please enter a valid age")

# # 5. Write a program that tracks the inventory of items in a store. The user should be able 
# # 	to add or remove items and the program should display the current inventory after each
# # 	operation. The program stops when the user decides to exit.
# # 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# # 	Sample Input and Output:
# # 	Enter operation (add/remove/exit): add
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
# #     operation = input("Enter operation (add/remove/exit): ").strip().casefold()
# #     if operation == "exit":
# #         break
# #     elif operation == operation.append:








# # Initial store inventory
# # inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

# # while True:
# #     operation = input("Enter operation (add/remove/exit): ").strip().lower()
    
# #     if operation == "exit":
# #         break 
    
# #     elif operation in ["add", "remove"]:
# #         item = input("Enter item: ").strip().lower()
# #         quantity = int(input("Enter quantity: "))  

# #         if operation == "add":
# #             inventory[item] = inventory.get(item, 0) + quantity 
        
# #         elif operation == "remove":
# #             if item in inventory and inventory[item] >= quantity:
# #                 inventory[item] -= quantity 
# #                 if inventory[item] == 0:
# #                     del inventory[item] 
# #             else:
# #                 print("Invalid operation. Not enough stock or item does not exist.")

# #         print("Current inventory:", inventory) 

# #     else:
# #         print("Invalid operation. Please enter 'add', 'remove', or 'exit'.")


# # text = input("Enter some text: ")
# # i = 0
# # # char = 1
# # counts = {}
# # while i < len(text):
# #     char = text[i]
# #     if char in counts:
# #         counts[char] += 1
# #     else:
# #         counts[char] = 1 
# #     i += 1

# # print(counts)


# text = input("Enter some text: ")
# i = 0
# counts = {"uppercase": 0, "lowercase": 0}
# while i < len(text):
#     char = text[i]
#     if char.isupper():
#         counts["uppercase"] += 1
#     elif char.islower():
#         counts["lowercase"] += 1
#     i+=1
# print(counts)


x = 0
s = 0
while (x < 10):
     s = s + x
     x = x + 1
else :
     print('The sum of first 9 integers : ',s)    




i = 0
d = 0
while i < 10:
    d +=i
    i +=1
print(d)
