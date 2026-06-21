# num_1 = 200
# num_2 = 200n {num_2}")
# elif num_1 == num_2:
#     print(f"{num_1} is equal to {num_2}")
# else:
#     print(f"{num_2} is greater than or equal to {num_1}")


# print("This print statement will run")


# is_raining = True


# if num_1 > num_2:
#     print(f"{num_1} is greater tha
# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("Carry sunglasses")


# name = input("What is your name? ").strip()


# if name:
#     print(f"Good morning, {name}")
# else:
#     print("Good morning, Anonymous")


# mode = "automatic"

# # if mode is automatic, then print "Automatic mode activated", else if mode is manual, 
# # print "Manual mode activated", otherwise, print "Invalid mode"

# if mode == "Automatic":
#     print("Automatic mode activated")
# elif mode == "Manual":
#     print("Manual mode activated")
# else:
#     print("Invalid mode")


# Ask the user for their name, If their name starts with a vowel, print "Your name starts with a vowel". Otherwise, print "Your name does not start with a vowel".
# name = input("What is your name?: ").casefold().strip()
# vowels = ("a", "e", "i", "o", "u")
# if name.startswith(vowels):
#     print("Your name starts with a vowel")
# else:
#     print("Your name does not start with a vowel")


# is_raining = False

# statement = "It is raining" if is_raining else "It is not raining"

# print(statement)

# if is_raining:
#     statement = "It is raining"
# else:
#     statement = "It is not raining"

# print(statement)



# has_umbrella = True
# has_raincoat = False


# print(not has_raincoat)

# if both are True, print "You are protected from the rain". If one is True, print "You are protected from the rain". 
# If neither is True, print "You are not protected from the rain"

# if has_umbrella and has_raincoat:
#     print("You are well protected from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print("You are not protected from the rain")




age = 17
is_male = True
has_voter_card = True


if is_male:
    if age < 18:
        print("You are male but you are not of age to vote")
    elif age >= 18:
        if has_voter_card:
            print("You are male and you are of age to vote and you have a voter's card. You can vote.")
        else:
            print("You are male and you are of age to vote but you do not have a voter's card. You cannot vote")
else:
    print("Women do not have the right to vote")


# def check_eligibility(age, is_male):
#     if not is_male:
#         return "Women do not have the right to vote"
    
#     if not has_voter_card:
#         return "You are male but you do not have a voter's card"
    
#     print("This will run")
    
#     if age >= 18:
#         return "You are male and you are of age to vote"
#     else:
#         return "You are male but you are not of age to vote"
    

# print(check_eligibility(18, True))
# def check_eligibility(age, is_male):
#     if is_male:
#         if age >= 18:
#             return "You are male and you are of age to vote"
#         else:
#             return "You are male but you are not of age to vote"
    
#     return "Women do not have the right to vote"
    

# print(check_eligibility(18, True))


# Given a string `message` entered by the user, use if statements to check if the message contains any 
# of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". 
# Otherwise, print "Normal message".

# "Good day. I have a message for the Dean"


# message = input("Enter the message: ").strip().casefold()

# if "urgent" in message or "important" in message or "immediate" in message:
# # if "urgent" or "important" or "immediate" in message:  # wrong
#     print("High priority message")
# else:
#     print("Normal message")


# high_priority_keywords = ("urgent", "important", "immediate")
# for keyword in high_priority_keywords:
#     if keyword in message:
#         print("high priority message")
#         break
# else:
#     print("Normal message")




message = input("Enter the message: ").strip().casefold()
word = (("urgent", "important", "immediate"))

if word == message:
    print("High priority message")
else:
    print("Normal message")

