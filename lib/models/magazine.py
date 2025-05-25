from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['id'], row['name'], row['category']) if row else None

    @classmethod
    def find_by_author_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (author_id,))
        magazines = [cls(row['id'], row['name'], row['category']) for row in cursor.fetchall()]
        conn.close()
        return magazines
