from .database import get_conn

def add(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO Student VALUES (?,?,?,?,?)", data)
    conn.commit()
    conn.close()

def update(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""UPDATE Student SET TenSV=?,NgaySinh=?,GioiTinh=?,TenLop=? WHERE MaSV=?""", data)
    conn.commit()
    conn.close()

def delete(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Student WHERE MaSV=?", (id,))
    conn.commit()
    conn.close()

def find(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Student WHERE MaSV=?", (id,))
    r = c.fetchone()
    conn.close()
    return r

def get_all():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Student")
    r = c.fetchall()
    conn.close()
    return r

def exists_by_id(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Student WHERE MaSV=?", (id,))
    r = c.fetchone()
    conn.close()
    return r is not None