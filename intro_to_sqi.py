import sqlite3
conn = sqlite3.connect("employees_db.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    yearjoined INTEGER NOT NULL,
    department TEXT NOT NULL
);
""")

# cursor.execute("""
# INSERT INTO employees (firstname, lastname, age, gender, yearjoined, department) VALUES
# (?,?,?,?,?,?),
# (?,?,?,?,?,?),
# (?,?,?,?,?,?)
# """, ("Bamidele", "Olamide", 10, "M", 2021, "STATISTICS","Ajay", "Purple", 22, "F", 2020, "Computer", "John", "Doe", 40, "M", 2019, "Data science"))


rows = cursor.execute(f"""
SELECT* FROM employees;
""").fetchall()
for row in rows:
    print(row)

cursor.execute(f"""
UPDATE employees
SET department = ? WHERE id = ?;
""",("Data analyst", 1))

conn.commit()


cursor.execute(f"""
DELETE FROM employees
WHERE id = ?;
""", (2,))
conn.commit()

record = cursor.execute(f"""
SELECT * FROM employees WHERE age > ? AND gender = ?;
""", (30, "M")).fetchall()

print(record)


conn.close()