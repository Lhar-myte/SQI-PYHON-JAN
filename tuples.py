# # my_tuple = ("timothy", "lusi", "teejay", "roqeeb", "adeoye", "lekan","olamide")
# # # print(my_tuple)
# # print(my_tuple[0:5])
# numbers = (1, 2, 3)
# one, two, three = numbers
# print("one:", 1)
# print("two:", 2)
# print("three:", 3)
#     # SET
# transportation = {"motorcycle", "train","boat", "ship","aircraft"}
# print(type(transportation))
# print(len(transportation))
# # print(transportation)
# # print(transportation[4])
# # print(bool[1])
# transportation = ["motorcycle", "train","boat", "ship","aircraft"]
# print(set(transportation))


# myself = {True,1}
# print(myself)
# myself = {False,0}
# print(myself)

# 1. Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
dimensions = (10, 20, 30)
length, width, height = dimensions
print("lenght:", 1)
print("width:", 2)
print("height:", 3)

# 2.Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.
coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(y)

# 3. Create a tuple called person with values ("John", 25, "Engineer"). 
# Unpack the values into variables name, age, and profession, and print the value of profession.
person = ("John", 25, "Engineer")
name, age, profession = person
print(profession)

# 4. Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
(student1, student2), _, _ = data
print(student2)

# 5. Create a tuple called colors with values ("red", "green", "blue", "yellow").
#  Unpack the first two values into variables color1 and color2, and print both variables.
colors = ("red", "green", "blue", "yellow")
color1, color2, _, _ = colors
print(color1)
print(color2)

# 6.Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. 
# Print the extracted age and the first department.
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, (age, _), (first_dpt, _) = record
print(age)
print(first_dpt)


# 7. Create a tuple called triplet with values ("one", "two", "three"). 
# Unpack the tuple into variables and print the value of the second variable.
triplet = ("one", "two", "three")
_, second, _ = triplet
print(second)

# 8.Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.

info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
product_ID, (category, price), manufacture_date = info
print(category)
_,_,year = manufacture_date
print(year)

# 9.Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). 
# Unpack the nested tuples into individual variables and print the second value of the third tuple.
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
_, _, (alphabet1, alphabet2) = nested_tuple
print(alphabet2)

# 10.Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
fruit1, fruit2, fruit3 = inventory
second_fruit, quantity = fruit2
print(quantity)

