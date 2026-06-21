# Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
fruits_list = ["apple", "banana", "orange"]
print(fruits_list[0])

# Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
colour = ["red", "green", "blue"]
print(colour[-1])

# Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])

# Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alphabets[-3::])

# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
ages = [20, 30, 40]
ages[1] = 35
print(ages)

# Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
grades = ["A", "B", "C", "D"]
grades[1:4] = ["x"]
print(grades)

# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
cities = ["New York", "London", "Paris"]
cities.insert(0, "Tokyo")
print(cities)

# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
prices = [10.5, 20.0, 15.75]
print(type(prices))

# Create a list called mixed with items 10, "apple", True. Print the list.
mixed_items = [10, "apple", True]
print(mixed_items)

# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
tuple_data = ("a", "b", "c")
tuple_list = list(tuple_data)
print(tuple_list)

# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
books = [ "Python", "Java"]
books.append("JavaScript")
print(books)

# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
names = ["Alice", "Bob", "Eve"]
names.insert(1, "Charlie")
print(names)

# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
students = ["Alice", "Bob"]
students_tupple = ("Charlie", "David")
students.extend(students_tupple)
print(students)

# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
colours_list = [ "red", "green", "blue"]
colours_list.remove("green")
print(colours_list)

# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
lists_numbers = [10, 20, 30, 40]
del lists_numbers[2]
print(lists_numbers)

# Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
fruits_lists = ["apple", "banana", "cherry"]
fruits_lists.clear()
print(fruits_lists)

# Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
names_lists = ["Zoe", "Alice", "Bob"]
names_lists.sort()
print(names_lists)

# Create a list called ages with items 25, 35, 20. Sort the list in descending order.
lists_ages = [ 25, 35, 20]
lists_ages.sort(reverse = True)
print(lists_ages)

# Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
words = ["Apple", "banana", "Orange"]
words.sort(key= str.lower)
print(words)

# Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
my_numbers = [1, 2, 3, 4]
my_numbers.reverse()
print(my_numbers)


# Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using slicing.
letters = ["a", "b", "c", "d"]

print(letters[::-1])

# Create a list called original with items "one", "two", "three". Create a copy of the list.
original = ["one", "two", "three"]
original_copy = original.copy()
print(original_copy)

# Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and list2 together.
listss1 = ["a", "b"]
listss2 = ["c", "d"]
new_list = (listss1) + (listss2)
print(new_list)

# Access and print the second subject of the first person in the list.
# 	data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
data = [
     ["Alice", 25, ["Math", "Physics"]],
     ["Bob", 30, ["Chemistry", "Biology"]],
     ["Charlie", 35, ["History", "Geography"]]
]

print(data[0][2][-1])

# Access and print the first value in the list of numbers associated with "San Francisco".
# 	records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
records = [
    ["New York", [10, 20, 30]],
    ["San Francisco", [40, 50, 60]],
    ["Austin", [70, 80, 90]]
]
print(records[1][1][0])
