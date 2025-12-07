import sqlite3

class Database:
    def __init__(self, path="academia.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS respostas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT,
                resposta TEXT,
                correcta INTEGER
            )
        """)
        self.conn.commit()

    def adicionar_resposta(self, pergunta, resposta, correcta):
        self.cursor.execute(
            "INSERT INTO respostas (pergunta, resposta, correcta) VALUES (?, ?, ?)",
            (pergunta, resposta, correcta)
        )
        self.conn.commit()

    def obter_respostas(self):
        self.cursor.execute("SELECT * FROM respostas")
        return self.cursor.fetchall()
