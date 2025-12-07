import sqlite3

class Database:
    def __init__(self, path="academia.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

        self.get_game()

    def get_game(self):
        self.cursor.execute("SELECT * FROM game")
        return self.cursor.fetchall()
