# shopping_list = ["eggs", "oil", "pepper", "onions", "salt", "cheese", "cheese"]
# print((shopping_list[0]))

# my_name = ["Winifred"]
# my_name[0] = "Y"
# print(my_name)

# print("Pepper" in shopping_list)

# shopping_list[1] = "butter"

# shopping_list.append("milk")

# # print("before remove: ", shopping_list)
# # shopping_list.remove("Onions")
# # print("after remove: ", shopping_list)


# my_list = [True, "87", 98.6, "Hello", False, 9]
# print(my_list)


# musical_instruments = ["drums", "guitar", "xylophone"]
# musical_instruments[1:2] = ["trumpet"]
# print(musical_instruments)

# print(musical_instruments[-1])


# my_name = "timothy"
# my_name = my_name.capitalize()
# print(my_name)


# currencies = ["naira", "dollar", "pounds", "euro", "Yen", "Lira", "rands"]
# print("Before insert: ", currencies)
# currencies.insert(2, "rubles")
# currencies.insert(5, "rupies")
# currencies.insert(3, "rupies")
# print("After insert: ", currencies)

# print(type(currencies))

# empty_list = []
# print(empty_list)

# letters = ("a", "j", "p")
# name = "Akintola"
# letters_list = list(name)
# print(letters_list)

# print(bool([]))
# print(bool(()))
# print(bool(""))
# print(bool(0))
# print(bool(-10))
# print(bool(["Rebecca", "Lekan", "Roqeeb"]))
# print(bool(("Rebecca", "Lekan", "Roqeeb")))


# currencies = ["naira", "dollar", "pounds", "euro", "Yen", "Lira"]
# currencies.append("rands")
# print(currencies)

# items = ["bag", "shoe", "watch", "phone"]
# other_items = ["bulb", "ring", "board", "drink"]
# remove watch from items and remove ring from other_items



# items.extend(other_items)
# print("items: ", items)
# print("other_items: ", other_items)

# tv inbetween shoe and watch
# detergent at the end of the list


# import random

# currencies = ["naira", "dollar", "pounds", "euro", "Yen", "Lira"]
# currencies = []
# random.shuffle(currencies)
# print(currencies)
# currencies.remove("naira")
# popped_item = currencies.pop(100)
# print("currencies: ", currencies)
# print("popped_item: ", popped_item)


# currencies = ["naira", "dollar", "pounds", "euro", "Yen", "Lira"]

# del currencies[0]
## del currencies

# print(currencies)

# GIL

# currencies = ["naira", "dollar", "pounds", "euro", "yen", "lira"]

# other_currencies = []

# currencies.clear()

# currencies.append("rupies")

# print("other_currencies: ", other_currencies)

# print("currencies before sort: ", currencies)
# currencies.sort(reverse=True)
# print("currencies after sort: ", currencies)


# numbers = [1, 11, "john", 8, 10]
# numbers.sort()
# # numbers.sort(reverse=True)
# print(numbers)


# numbers = [1, 11, "john", 8, 10]

# numbers.reverse()
# numbers = numbers[::-1]
# print(numbers)

# import copy

# currencies = ["naira", "dollar", "pounds", "euro", "yen", "lira"]
# # currencies_copy = currencies
# currencies_copy = copy.deepcopy(currencies)

# # currencies_copy = currencies.copy()

# currencies_copy.append("rupies")
# print("currencies: ", currencies)
# print("currencies_copy: ", currencies_copy)

# gotcha



# items = ["bag", "shoe", "watch", "phone"]
# other_items = ["bulb", "ring", "board", "drink"]

# all_items = items + other_items


# print(all_items)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][2])


nested_list = [
    ["Alice", "Bob"],
    [10, 20, 30],
    [True, False]
]

# print(nested_list[1][0] + nested_list[1][2])
# print(int(nested_list[-1][0]))
nested_list[2][1] = True
print(nested_list)