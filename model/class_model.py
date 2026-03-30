from .database import get_conn

def add(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO Class VALUES (?,?)", data)
    conn.commit()
    conn.close()

def update(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE Class SET TenLop=? WHERE MaLop=?", data)
    conn.commit()
    conn.close()

def delete(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Class WHERE MaLop=?", (id,))
    conn.commit()
    conn.close()

def find(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Class WHERE MaLop=?", (id,))
    r = c.fetchone()
    conn.close()
    return r

def get_all():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Class")
    r = c.fetchall()
    conn.close()
    return r