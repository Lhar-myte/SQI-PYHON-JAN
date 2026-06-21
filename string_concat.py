# # Good morning, January Cohort
# greetings = "Good morning"
# cohort = "January cohort"



# print(greetings + ", " + cohort )


name = "Rebecca"
age = 45
height = 6.5
is_male = False


# print("My name is " + name + ", I am " + str(age) + "years old" + "\nI am " + str(height) + "feet tall. " + "It is " + str(is_male) + " that I am a Male")

print(f"My name is {name}, I am {age} years old. I am {height} feet tall. It is {is_male} that I am a Male")



text = "My name is {}, I am {}years old. I am {} feet tall. It is {} that I am a Male".format(name, age, height, is_male)
print(text)

print(text)

# https://google.com

# domain_name = "google"
# print("https://" + domain_name + ".com")


# The [Adjective] [Noun] likes to [Verb]


# adjective = "beautiful"
# noun = "Rebecca"
# verb = "swim"

# print(f"The {adjective} {noun} likes to {verb}")



print("rebecca".capitalize())





# time_of_day = "morning"
# mood = "happy"
# arrival = 9
# is_student = True

# Good morning. I am happy today. I got to SQI by 9 today. It is True that I am a student.




# text = "Hello World"
# print(text[5])





# text = "my name is {}, I am {}years old. I am {} feet tall. It is {} that I am a Male".format(name, age, height, is_male).capitalize()
# print(text)



full_name = "richie mighty"

capitalized_name = full_name.capitalize()
titled_name = full_name.title()

print(full_name)
print(capitalized_name)
print(titled_name)


full_name = "richiemighty".split("e")

print(full_name)



# names =  ["Lusi", "Heritage", "Rebecca", "Timothy", "Olamide"]
# second_ind = names[1]
# g_from_heri = second_ind[-2]
# print(g_from_heri)



artist = "richard"
print(artist.find("r", 3))




# print(artist.index('mo'))

# num1 = int(input(Enter your age))
# print(num1)



x = 6
y = 4

print(x < y)
print(type(x < y))
# x != y --- x is not equal to y 
print(type(x != y))     

price = 25.9
age = 89
print(age > price)
print(age != price)
print(age >= price)

x = y = z = 5
print(x)
print(y)
print(z)

name = 'richard', 'olamide'
first_name = name[0]
first_name, second_name = name
# print(first_name, end(""))
# print(first_name, /n)


fruit = 'apple', 20.38, 30
# fruit_name = fruit[0]
# fruit_price = fruit[1]
# fruit_count = fruit[2]
fruit_name, fruit_price, fruit_count = fruit
print(fruit_name)
print(fruit_price)
print(fruit_count)