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


rows = cursor.execute(f"""
SELECT * FROM students;
""").fetchall()

for row in rows:
    print(row)


cursor.execute("""
UPDATE students SET age = ? WHERE id = ?;
""", (20, 3))

conn.commit()

cursor.execute("""
DELETE FROM students WHERE id = ?;
""", (2,))

conn.commit()

conn.close()