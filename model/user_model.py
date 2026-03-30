from .database import get_conn

def register(email, password):
    conn = get_conn()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users(email,password) VALUES (?,?)",(email,password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login(email, password):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password))
    r = c.fetchone()
    conn.close()
    return r