# name = input()
# print(name)

# name = input("What is your name? ")
# print(name)

# name = input("What is your name? ")
# print(f'Hello, {name}')

# name = input("What is your full name? ")
# print(type(name))
# print(f'Hello, {name}')
# names = "ola baddo"
# names = name.split(" ")
# first_name = names[0]
# second_name = names[1]
# print(f"Your first name is {first_name} and your second name is {second_name}")

# first_name, last_name = input("What is your full name? ").split(" ")
# print(f"Your first name is {first_name} and your last name is {second_name}")


from getpass import getpass

# password = getpass("Enter your password: ")
# print(password)

password = input("Enter your password: ")
print(password)

new_password = input("Enter a new password: ")
print(new_password)

print(password == new_password)

if password == new_password:
    print("log in")
else:
    print("try again")
