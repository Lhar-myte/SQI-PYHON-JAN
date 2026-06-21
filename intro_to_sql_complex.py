import sqlite3

conn = sqlite3.connect("students_db.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
);
""")

# i = 1
# while True:
#     name = input(f"Enter the name of student {i}: ").strip()
#     age = int(input(f"Enter the age of student {i}: "))
#     gender = input(f"Enter the gender of student {i}: ").strip()

#     cursor.execute("""
#     INSERT INTO students (name, age, gender) VALUES
#     (?, ?, ?)  
#     """, (name, age, gender))

#     conn.commit()

#     i += 1

#     enter_next_record = input(f"Do you want to enter the details of student {i} (yes/no): ").strip()

#     if enter_next_record != "yes":
#         break

# cursor.execute("""
# INSERT INTO students (name, age, gender) VALUES
# (?, ?, ?),     
# (?, ?, ?),     
# (?, ?, ?),     
# (?, ?, ?),     
# (?, ?, ?),     
# (?, ?, ?),     
# (?, ?, ?),     
# (?, ?, ?)  
# """, ("Mrs. Akintola Soburat", 10, "F", "Lusi Otunba", 29, "M", "Bamidele Olamide", 16, "M", "Ajayi Rebecca", 12, "F", "Okonkwo Timothy", 50, "M", "Adeniyi Adeoye", 76, "M", "Akanbi Lekan", 90, "M", "Oyedeji TJ", 11, "M"))


# sql injection attack

def fetch_all_students(fetch_name=False, fetch_age=False, fetch_gender=False):
    columns_to_fetch = []

    if fetch_name:
        columns_to_fetch.append("name")
    if fetch_age:
        columns_to_fetch.append("age")
    if fetch_gender:
        columns_to_fetch.append("gender")

    if not columns_to_fetch:
        columns_to_fetch = "*"
    else:
        columns_to_fetch = ", ".join(columns_to_fetch)


    rows = cursor.execute(f"""
    SELECT {columns_to_fetch} FROM students;
    """).fetchall()

    # print(rows)

    for row in rows:
        print(row)


cursor.execute("""
UPDATE students
SET age = ?
WHERE id = ?;
""", (20, 3))

conn.commit()

cursor.execute("""
DELETE FROM students
WHERE id = ?;
""", (2, ))

conn.commit()

fetch_all_students(fetch_name=True)


conn.close()