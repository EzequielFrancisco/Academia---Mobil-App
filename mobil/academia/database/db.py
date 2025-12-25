import sqlite3

class Database:
    def __init__(self, path="academia.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

        self.get_game()

    def get_game(self):
        self.cursor.execute("SELECT * FROM game")
        return self.cursor.fetchall()

    def insert_game(self, module, question, options, correct):
        options_str = "|".join(options)

        query = "INSERT INTO game (module_code, questions, options, correct) VALUES (?, ?, ?, ?)"
        values = (module, question, options_str, correct)

        self.cursor.execute(query, values)
        self.conn.commit()
