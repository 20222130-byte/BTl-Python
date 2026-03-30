from .database import get_conn

def add(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO Scores VALUES (?,?,?,?)", data)
    conn.commit()
    conn.close()

def update(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE Scores SET Toan=?,Van=?,Anh=? WHERE MaSV=?", data)
    conn.commit()
    conn.close()

def delete(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Scores WHERE MaSV=?", (id,))
    conn.commit()
    conn.close()

def find(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Scores WHERE MaSV=?", (id,))
    r = c.fetchone()
    conn.close()
    return r

def get_all():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Scores")
    r = c.fetchall()
    conn.close()
    return r