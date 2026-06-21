import re
import sqlite3
import hashlib

from getpass import getpass

conn = sqlite3.connect("customers.db")

def main():
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)


    def sign_up():
        print("\n********************Sign Up********************\n")

        while True:

            first_name = input("Enter your first name: ").strip().capitalize()

            if not first_name:
                print("FIrst name field is required")
                continue

            break

        while True:

            last_name = input("Enter your last name: ").strip().capitalize()
            if not last_name:
                print("Last name field is required")
                continue

            break

        
        while True:
            username = input("Enter your username: ").strip().capitalize()
            if not username:
                print("Username field is required")
                continue
            break

        while True:
            try:
                age = int(input("Enter your age: "))
            except ValueError:
                print("Age must be a number")
                continue
            break

        while True:
            email = input("Enter your email address: ").strip()
            email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            email_is_valid = re.match(email_pattern, email)
            if not email_is_valid:
                print("Enter a valid email address")
                continue
            break

        while True:
            password = getpass("Enter your password: ").strip()
            if not password:
                print("Password field is required")
                continue

            confirm_password = getpass("Confirm your password: ").strip()
            if not confirm_password:
                print("Confirm Password field is required")
                continue


            if password != confirm_password:
                print("Passwords do not match")
                continue
        
            break
        

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            cursor.execute("""
            INSERT INTO customers (first_name, last_name, username, age, email, password) VALUES 
            (?, ?, ?, ?, ?, ?);
            """, (first_name, last_name, username, age, email, hashed_password))
        except sqlite3.IntegrityError:
            print("A user with that username already exists.")
            return None
        else:
            print("Sign up successful")
            conn.commit()
            log_in()

    def log_in():

        print("\n********************Log In********************\n")
        
        username = input("Enter your username: ").strip().capitalize()
        password = getpass("Enter your password: ").strip()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        user = cursor.execute("""
        SELECT * FROM customers WHERE username = ? AND password = ?;
        """, (username, hashed_password)).fetchone()

        if user is None:
            print("Invalid username or password.")
            return None
        else:
            print("Log in Successful")
            return checkout(user)


    def checkout(user):
        print("\n********************Checkout********************\n")

        _, first_name, last_name, _, _, _, _ = user
        print(f"Welcome {first_name} {last_name}")
        print("Accessing Checkout feature")



    menu = """
1. Sign Up.
2. Log In.
3. Quit.
"""

    while True:
        print(menu)
        choice = input("Choose an option from the menu above: ").strip()
        if choice == "3":
            print("Exiting the program")
            break

        if choice not in ["1", "2"]:
            print("Invalid choice")
            continue

        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        
try:
    main()
except Exception:
    conn.close()