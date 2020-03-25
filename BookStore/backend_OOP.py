import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, b_id INTEGER)")
        self.conn.commit()
        

    def insert(self, title, author, year, b_id):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, b_id))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

#By default we are putting "blank strings" to the function arguments, because they are not all mandatory
    def search(self, title="", author="", year="", b_id=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR b_id = ?", (title, author, year, b_id))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, newTitle, newAuthor, newYear, newB_id):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, b_id = ? WHERE id = ?", (newTitle, newAuthor, newYear, newB_id, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#insert ("40 Pravila ljubavi", "Elif Safak", 2018, 98722298)
#delete(2)
#update(1, "40 pravila", "Elif", 2019, 33399933)
#print(view())