from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data

data = read_data("data.txt")
for name, age in data:
    print(f"Name: {name}, Age: {age}" )
usernames = fetch_user_data()
for i, username in enumerate(usernames, start=1):
    print(f"{i}. {username}")
