import sqlite3
from faker import Faker
import random

# Create database
conn = sqlite3.connect('test_university.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE students
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER
    )
''')

cursor.execute('''CREATE TABLE groups
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
''')

cursor.execute('''CREATE TABLE lectors
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
    ''')

cursor.execute('''CREATE TABLE subjects
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lector_id INTEGER NOT NULL
    )          
    ''')

cursor.execute('''CREATE TABLE grades
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
    )
    ''')

# Table waste
fake = Faker()

# Table groups waste
for _ in range(3):
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (fake.random_element(['A', 'B', 'C', 'D', 'F']),))

# Table students waste
for _ in range(50):
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (fake.name(), random.randint(1, 3)))

# Table lectors waste
for _ in range(5):
    cursor.execute("INSERT INTO lectors (name) VALUES (?)", (fake.name(),))

# Table subjects waste
for _ in range(8):
    cursor.execute("INSERT INTO subjects (name, lector_id) VALUES (?, ?)", (fake.random_element(
        ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Computer Science', 'Art']
        ), random.randint(1, 5)))
    
# Table grades waste
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        for _ in range(5):
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)", (student_id, subject_id, random.randint(60, 100)))

conn.commit()
conn.close()