import MySQLdb
import ulid

class DB():
    def __init__(self):
        self.conn = MySQLdb.connect(
            user = 'user',
            passwd = 'password',
            host = 'localhost',
            db = 'mydb',
            charset = 'utf8'
        )
        self.c = self.conn.cursor()

    def close(self):
        self.c.close()
        self.conn.close()
    
    def add(self, new_book: dict):
        self.c.execute("""insert into books (id, title, author)
                       values (%s, %s, %s)""", (ulid.new(), new_book['title'], new_book['author'],))
        self.conn.commit()
        self.close()
        
    
    def findAll(self):
        self.c.execute("""select id, title, author from books;""")
        books = self.c.fetchall()
        res = []
        for book in books:
            res.append({
                "id": book[0],
                "title": book[1],
                "author": book[2]
            })
        self.close()
        return res