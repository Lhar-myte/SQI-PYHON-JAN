import requests

def fetch_user_data():
    user_data = requests.get("https://jsonplaceholder.typicode.com/users").json()

    usernames = []
    for data in user_data:
        usernames.append(data["username"])

    return usernames