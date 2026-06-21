class BankAccount:
    def __init__(self, account_owner, account_number, bank_name, bvn, balance):
        self.owner = account_owner
        self.account_num = account_number
        self.bank_name = bank_name
        self.bvn = bvn
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "insufficient funds"
        self.balance -= amount 
        return f"withdrawal successful. Current balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount 
        return f"Deposit successful. Current balance: {self.balance}"
    

olamide_acct = BankAccount("Bamidele Olamide Samuel", "3141955477", "First Bank", "2345678987", 50000.00)
timothy_acct = BankAccount("Okonkwo Timothy", "8057659360", "Opay", "23456789", 100000.00)

print(timothy_acct.bank_name)
print(olamide_acct.withdraw(5000000))
print(olamide_acct.bvn)


olamide_primitive_acct = {"owner": "Bamidele Olamide Samuel", "account_num": "3141955477", "bank_name": "First Bank", "bvn": "2345678987", "balance": 50000.00}
timothy_primitive_acct = {"owner": "Okonkwo Timothy", "account_num": "8057659360", "bank_name": "Opay", "bvn": "23456789", "balance": 100000.00}

def withdraw(amount, acct):
    if amount > acct["balance"]:
        return "insufficient funds"
    acct["balance"] -= amount 
    return f"withdrawal successful. Current balance: {acct["balance"]}"

def deposit(amount, acct):
    acct["balance"] += amount 
    return f"Deposit successful. Current balance: {acct["balance"]}"

print(timothy_primitive_acct["bank_name"])
print(withdraw(5000, olamide_primitive_acct))
print(olamide_primitive_acct["bvn"])

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


class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

class Notebook:
    def __init__(self, notes: list):
        self.notes = notes

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                return f"{note.title} removed"
        return f"Note with id {note_id} does not exist"

    def display_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return f"""
{note.title}
{note.content}
"""
        return f"Note with id {note_id} does not exist"

    def display_all_notes(self):
        for note in self.notes:
            print(note.title)
            print(note.content)
            print("\n")   

to_do = Note(1, "To do List", """
1. Wash plates.
2. Cook indomie
3. Sleep
4. Watch movies.
""")

shopping_list = Note(2, "Shopping List", """
1. Tomato paste.
2. Chicken
3. Groundnut oil
4. Rice
5. Ginger
6. Garlic
7. Maggi
8. Salt
9. Bayleaf
""")

notebook = Notebook([to_do])
notebook.add_note(shopping_list)
# notebook.display_all_notes()
# print(notebook.delete_note(10))
print(notebook.display_note(2))
# notebook.add_note(to_do)
# notebook.display_all_notes()