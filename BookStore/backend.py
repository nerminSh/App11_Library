import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, b_id INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, b_id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, b_id))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

#By default we are putting "blank strings" to the function arguments, because they are not all mandatory
def search(title="", author="", year="", b_id=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR b_id = ?", (title, author, year, b_id))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, newTitle, newAuthor, newYear, newB_id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, b_id = ? WHERE id = ?", (newTitle, newAuthor, newYear, newB_id, id))
    conn.commit()
    conn.close()

connect()
#insert ("40 Pravila ljubavi", "Elif Safak", 2018, 98722298)
#delete(2)
#update(1, "40 pravila", "Elif", 2019, 33399933)
#print(view())