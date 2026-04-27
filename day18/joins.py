import sqlite3
import pandas as pd
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern_name TEXT,
    track TEXT
)""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
)""")
cursor.execute("DELETE FROM interns")  
cursor.execute("DELETE FROM mentors")
intern_data = [
    ('Rahul', 'Data Science'),
    ('Sneha', 'Web Development'),
    ('Aman', 'Data Science'),
    ('Priya', 'Cyber Security')
]
mentor_data = [
    ('Mr. Sharma', 'Data Science'),
    ('Ms. Kavya', 'Web Development'),
    ('Mr. Khan', 'Cyber Security')
]
cursor.executemany("INSERT INTO interns (intern_name, track) VALUES (?, ?)", intern_data)
cursor.executemany("INSERT INTO mentors (mentor_name, track) VALUES (?, ?)", mentor_data)
conn.commit()
query = """
SELECT 
    interns.intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""
df = pd.read_sql_query(query, conn)
print("JOIN Result:\n")
print(df)
conn.close()