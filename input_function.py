# first_name, second_name = input("What is your full name? ").split(" ")
# print(f"Your first name is {first_name.title()} and your second name is {second_name.title()}")
# 
# names = name.split(" ")
# print(name)
# print(names)

# first_name = names[0]
# second_name = names[1]

# print(f"Your first name is {first_name.title()} and your second name is {second_name.title()}")


from getpass import getpass

password = input("Enter your password: ")
print(password)

new_password = input("Enter a new password: ")
print(new_password)


if password == new_password:
    print("Log in")
else:
    print("Try again")