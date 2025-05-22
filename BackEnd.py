# BackEnd.py
import sqlite3

def connect():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            diagnosis TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_patient(name, age, gender, diagnosis):
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO patients (name, age, gender, diagnosis) VALUES (?, ?, ?, ?)", (name, age, gender, diagnosis))
    conn.commit()
    conn.close()

def view_patients():
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_patient(id, name, age, gender, diagnosis):
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("UPDATE patients SET name=?, age=?, gender=?, diagnosis=? WHERE id=?", (name, age, gender, diagnosis, id))
    conn.commit()
    conn.close()

def delete_patient(id):
    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE id=?", (id,))
    conn.commit()
    conn.close()
