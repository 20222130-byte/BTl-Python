import sqlite3

def get_conn():
    return sqlite3.connect("student.db")

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Class(
        MaLop TEXT PRIMARY KEY,
        TenLop TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Student(
        MaSV INTEGER PRIMARY KEY,
        TenSV TEXT,
        NgaySinh TEXT,
        GioiTinh TEXT,
        TenLop TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Scores(
        MaSV INTEGER PRIMARY KEY,
        Toan REAL,
        Van REAL,
        Anh REAL
    )""")

    conn.commit()
    conn.close()