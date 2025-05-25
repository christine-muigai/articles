from lib.db.connection import get_connection

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, (self.title, self.author_id, self.magazine_id))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    @classmethod
    def find_by_author_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        articles = [cls(row['id'], row['title'], row['author_id'], row['magazine_id']) for row in cursor.fetchall()]
        conn.close()
        return articles