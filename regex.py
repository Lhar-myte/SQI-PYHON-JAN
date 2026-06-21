import re

# # Example 1: Simple match
# pattern = r"\bword\b"
# text = "A word in a sentence."
# match = re.search(pattern, text)
# print(match)
# if match:
#     print("Match found:", match.group())  # Match found: word
# else:
#     print("match not found")



# pattern = r"\d+"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)

# print(matches)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']


# pattern = r"\s+"
# text = "This   is a test."
# new_text = re.sub(pattern, "", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.


# Example 1: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# text = "Contact us at support@example.com for more info."
# match = re.search(pattern, text)
# if match:
#     print("Email found:", match.group())  # Email found: support@example.com


# # Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']


# Example 3: Validate a phone number (US format)
# pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
# phone_number = "(123) 456-7890"
# if re.match(pattern, phone_number):
#     print("Valid phone number")  # Valid phone number
# else:
#     print("Invalid phone number")


# Example 4: Split a string by commas and whitespace
# pattern = r"\s*,\s*"
# text = "apple, banana ,  cherry,  date"
# fruits = re.split(pattern, text)
# print("Fruits list:", fruits)  # Fruits list: ['apple', 'banana', 'cherry', 'date']


# Example 6: Capture groups of text
# pattern = r"([\w-]+)@(\w+\.\w+)"
# text = "Emails: ali-ce@example.com, bob@domain.org"
# matches = re.findall(pattern, text)

# print(matches)

# for user, domain in matches:
#     print("User:", user, "Domain:", domain)

# Output:
# User: alice Domain: example.com
# User: bob Domain: domain.org


# Example 7: Using named groups
# pattern = r"(?P<user>\w+)@(?P<domain>\w+\.\w+)"
# text = "Contact: john.doe@company.com"
# match = re.search(pattern, text)
# if match:
#     print("User:", match.group("user"))  # User: doe
#     print("Domain:", match.group("domain"))  # Domain: company.com


# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']

# import re
# # Example 8: Compiling a regex for reuse
# pattern = re.compile(r"\b\w{4}\b")
# text = "This is a test of regex patterns."
# matches = pattern.findall(text)
# print("Four-letter words:", matches)  # Four-letter words: ['This', 'test']


