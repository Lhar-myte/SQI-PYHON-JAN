# class BankAccount:
#     def __init__(self, account_owner, account_number, bank_name, bvn, balance):
#         self.owner = account_owner
#         self.account_num = account_number
#         self.bank_name = bank_name
#         self.bvn = bvn
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "insufficient funds"
#         self.balance -= amount 
#         return f"withdrawal successful. Current balance: {self.balance}"
    
#     def deposit(self, amount):
#         self.balance += amount 
#         return f"Deposit successful. Current balance: {self.balance}"
    

# olamide_acct = BankAccount("Bamidele Olamide Samuel", "3141955477", "First Bank", "2345678987", 50000.00)
# timothy_acct = BankAccount("Okonkwo Timothy", "8057659360", "Opay", "23456789", 100000.00)

# print(timothy_acct.bank_name)
# print(olamide_acct.withdraw(5000000))
# print(olamide_acct.bvn)


# olamide_primitive_acct = {"owner": "Bamidele Olamide Samuel", "account_num": "3141955477", "bank_name": "First Bank", "bvn": "2345678987", "balance": 50000.00}
# timothy_primitive_acct = {"owner": "Okonkwo Timothy", "account_num": "8057659360", "bank_name": "Opay", "bvn": "23456789", "balance": 100000.00}

# def withdraw(amount, acct):
#     if amount > acct["balance"]:
#         return "insufficient funds"
#     acct["balance"] -= amount 
#     return f"withdrawal successful. Current balance: {acct["balance"]}"

# def deposit(amount, acct):
#     acct["balance"] += amount 
#     return f"Deposit successful. Current balance: {acct["balance"]}"

# print(timothy_primitive_acct["bank_name"])
# print(withdraw(5000, olamide_primitive_acct))
# print(olamide_primitive_acct["bvn"])

# class Student:
#     def __init__(self, name, age, sex, matric_no, dept, faculty, level, cgpa):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.matric_no = matric_no
#         self.dept = dept
#         self.faculty = faculty
#         self.level = level
#         self.cgpa = cgpa

#     def introduce_yourself(self):
#         gender = "Male" if self.sex == "M" else "Female"
#         return f"My name is {self.name} and I am {gender}. I am {self.age} years old. My matric number is {self.matric_no}. I am in {self.level} level in {self.dept} department of {self.faculty} faculty. My CGPA is {self.cgpa}."
    

# heritage = Student("Aina Heritage", 100, "F", "20190204017", "Computer Science", "Education", "400", 5.0)
# rebecca = Student("Ajayi Rebecca Odunayo", 45, "F", "HND/22012", "Statistics", "Science", "HND 2", 3.9)
# olamide = Student("Bamidele Olamide Samuel", 21, "M", "HND/22014", "Statistics", "Science", "HND 2", 2.5)

# print(heritage.introduce_yourself())
# print(rebecca.introduce_yourself())
# print(olamide.introduce_yourself())

# Create an Animal Class with the following attributes: name, type, color, is_mammal, sound
# and the following actions: speak
# Create 2 objects out of the class 

# class Animal:
#     def __init__(self, name, type, color, is_mammal, sound):
#         self.name = name
#         self.type = type
#         self.color = color
#         self.is_mammal = is_mammal
#         self.sound = sound

#     def speak(self):
#         return f"{self.name} says {self.sound}!"
    

# simba = Animal("Simba", "lion", "brown", True, "roar")
# nibbles = Animal("Nibbles", "mouse", "grey", True, "squeak")

# print(simba.speak())
# print(nibbles.speak())


# class Circle:

#     PI = 22/7

#     def __init__(self, radius):
#         self.radius = radius
#         self.circumference = 2 * Circle.PI * self.radius
#         self.diameter = 2 * self.radius


# circle_one = Circle(7)
# # print(circle_one.circumference)
# # print(circle_one.diameter)
# print(circle_one.PI)
# circle_two = Circle(10)
# print(circle_two.PI)


# Create a Cart class that will contain a list of items. 
# Each Item would be created out of the Item Class
# The Item class would have attributes: id, name, quantity, price
# The Cart class would have actions: add_item, remove_item, calculate_total

# class Item:
#     def __init__(self, id, name, quantity, price):
#         self.id = id
#         self.name = name
#         self.quantity = quantity
#         self.price = price

#     def __str__(self):
#         return f"{self.name} x{self.quantity}. Price: {self.price}"
    
# class Cart:
#     def __init__(self, items: list):
#         self.items = items

#     def add_item(self, item):
#         self.items.append(item)
    
#     def remove_item(self, item):
#         self.items.remove(item)

#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item.quantity * item.price
#         return total
    
# oil = Item(1, "Kings Oil", 7, 2500)
# print(oil)
# milk = Item(2, "Loya", 100, 150)
# print(milk)
# sugar = Item(3, "Dangote Sugar", 60, 200)
# print(sugar)


# shopping_cart = Cart([])
# shopping_cart.add_item(oil)
# shopping_cart.add_item(sugar)

# shopping_cart.add_item(milk)

# shopping_cart.remove_item(oil)

# print(shopping_cart.calculate_total())


# Create a Notebook class that will have an attribute 
# called notes which is a list of Note items.
# The Note class will have attributes: id, title, content
# The Notebook class will have the following
# actions: add_note(self, note), delete_note(self, note_id), 
# display_note(self, id) and display_all_notes(self).


# class Note:
#     def __init__(self, id, title, content):
#         self.id = id
#         self.title = title
#         self.content = content

# class Notebook:
#     def __init__(self, notes: list):
#         self.notes = notes

#     def add_note(self, note):
#         self.notes.append(note)

#     def delete_note(self, note_id):
#         for note in self.notes:
#             if note.id == note_id:
#                 self.notes.remove(note)
#                 return f"{note.title} removed"
#         return f"Note with id {note_id} does not exist"

#     def display_note(self, note_id):
#         for note in self.notes:
#             if note.id == note_id:
#                 return f"""
# {note.title}
# {note.content}
# """
#         return f"Note with id {note_id} does not exist"

#     def display_all_notes(self):
#         for note in self.notes:
#             print(note.title)
#             print(note.content)
#             print("\n")   

# to_do = Note(1, "To do List", """
# 1. Wash plates.
# 2. Cook indomie
# 3. Sleep
# 4. Watch movies.
# """)

# shopping_list = Note(2, "Shopping List", """
# 1. Tomato paste.
# 2. Chicken
# 3. Groundnut oil
# 4. Rice
# 5. Ginger
# 6. Garlic
# 7. Maggi
# 8. Salt
# 9. Bayleaf
# """)

# notebook = Notebook([to_do])
# notebook.add_note(shopping_list)
# # notebook.display_all_notes()
# # print(notebook.delete_note(10))
# print(notebook.display_note(2))
# # notebook.add_note(to_do)
# # notebook.display_all_notes()


# 1
# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2

#     def distance(self):
#         return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** 0.5

#     def slope(self):
#         return (self.y2 - self.y1) / (self.x2 - self.x1)

# # EXAMPLE EXECUTION

# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6


# 2
# class Cylinder:

#     PI = 3.14

#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return Cylinder.PI * (self.radius ** 2) * self.height

#     def surface_area(self):
#         return (2 * Cylinder.PI * self.radius * self.height) + (2 * Cylinder.PI * (self.radius ** 2))

# # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2



# 3
# class Account: 
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def format_money(self, money):
#         return "₦{:,.2f}".format(money)

#     @property
#     def formatted_balance(self):
#         return self.format_money(self.balance)

#     def __str__(self):
#         return f"""Account owner: {self.owner}
# Account balance: {self.formatted_balance}
# """    
    
#     def deposit(self, amount):
#         if amount <= 0:
#             return "Amount must be positive"
#         self.balance += amount
#         return "Deposit accepted"
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Amount must be positive"
        
#         if amount > self.balance:
#             return f"Funds Unavailable. You need {self.format_money(amount - self.balance)} more to complete that transaction"
        
#         self.balance -= amount
#         return "Withdrawal accepted"


# #1. Instantiate the class
# acct1 = Account('Winnie', 100)

# #2. Print the object
# print(acct1)
# print(acct1.formatted_balance)
# # Output:
# # Account owner: Winnie
# # Account balance: $100

# #3. Show the account owner attribute
# print(acct1.owner)  # Winnie

# #4. Show the account balance attribute 
# print(acct1.formatted_balance)  # 100

# #5. Make a series of deposits and withdrawals 
# print(acct1.deposit(50))  # Output: Deposit Accepted

# print(acct1.withdraw(15))  # Output: Withdrawal Accepted

# #6. Make a withdrawal that exceeds the available balance 
# print(acct1.withdraw(500))  # Output: Funds Unavailable!

# print(acct1.balance)
# print(acct1.formatted_balance)


# class Parent:
#     pass

# class Child(Parent):
#     pass

# print(issubclass(Parent, Child))



# class Animal:
#     def __init__(self, name, color, sound, is_mammal):
#         self.name = name
#         self.color = color
#         self.sound = sound
#         self.is_mammal = is_mammal

#     def introduce_yourself(self):
#         # self.number = 12

#         animal_is_mammal = "I am" if self.is_mammal else "I am not"

#         return f"My name is {self.name} and I have {self.color} color. I make a {self.sound} sound. {animal_is_mammal} a mammal."
    

# class Dog(Animal):
#     def __init__(self, name: str, color: str, sound: str, breed: str):
#         super().__init__(name, color, sound, True)
#         self.breed = breed

    
# lion = Animal("Mufasa", "brown", "roar", True)
# lion.introduce_yourself()
# print(lion.number)

# lion = Animal("Mufasa", "brown", "roar", True)
# dog = Dog("Lala", "white", "woof", "Husky")

# print(dog.is_mammal)
# print(lion.introduce_yourself())
# print(dog.introduce_yourself())


# class Device:
#     def operate(self):
#         return "Operating the device"
    
# class IPhone(Device):
#     def operate(self):
#         return "Operating the iPhone"
    
# class Samsung(Device):
#     def operate(self):
#         return "Operating the Samsung"
    
# class Itel(Device):
#     pass

# my_device = Device()
# iphone = IPhone()
# samsung = Samsung()
# itel = Itel()

# devices = [my_device, iphone, samsung, itel]
# device: Device
# for device in devices:
#     print(device.operate())

# print(my_device.operate())
# print(iphone.operate())
# print(samsung.operate())
# print(itel.operate())


# print(isinstance(5.0, float))

# class Person:
#     def __init__(self, name):
#         self.name = name

#     # def __str__(self):
#     #     return self.name
    
# rebecca = Person("Ajayi Rebecca")
# print(rebecca)


# class Animal:
#     def __init__(self, name, color, sound, is_mammal):
#         self.name = name
#         self.color = color
#         self.sound = sound
#         self.is_mammal = is_mammal

#     # def __str__(self):
#     #     return f"Animal named {self.name}"
    
#     def __repr__(self):
#         return f"Animal({self.name!r}, {self.color!r}, {self.sound!r}, {self.is_mammal})"
    
# cat = Animal(name="Fido", color="black", sound="meow", is_mammal=True)
# cat = Animal('Fido', 'black', 'meow', True)
# print(cat)

# class Book:
#     def __init__(self, title, author, year_published, no_of_pages, genre, isbn, content):
#         self.title = title
#         self.content = content
#         self.author = author
#         self.year_published = year_published
#         self.no_of_pages = no_of_pages
#         self.genre = genre
#         self.isbn = isbn

#     def __len__(self):
#         return len(self.content)

# and_then_there_were_none = Book("And then there were None", "Agatha Christie", 1967, 400, "Fiction", "ISBN 686 689 665", """
# This book was written by Agatha Christie. It is a murder fiction novel.
# """)
# print(len(and_then_there_were_none))



# class MyCustomList:
#     def __init__(self, *items):
#         self.items = list(items)

#     def __str__(self):
#         return str(self.items)
    
#     def __len__(self):
#         return len(self.items)

#     def append(self, item):
#         self.items.append(item)

#     def delete(self, item):
#         self.items.remove(item)
    
#     def append_many(self, *items):
#         self.items += list(items)

#     def pop_last_item(self):
#         return self.items.pop()
    

# my_custom_list = MyCustomList(1, 2, 3, 4)
# print(len(my_custom_list))
# my_custom_list.append("ten")
# print(my_custom_list)
# my_custom_list.delete(4)
# print(my_custom_list)
# my_custom_list.append_many(4, 5, 6, 7)
# print(my_custom_list)
# popped_item = my_custom_list.pop_last_item()
# print(my_custom_list)


