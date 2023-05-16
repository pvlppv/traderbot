import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_task(self, symbol, target_price):
        with self.connection:
            return self.cursor.execute(
                'INSERT INTO "tasks" ("symbol", "target_price") VALUES (?, ?)',
                (
                    symbol,
                    target_price,
                ),
            )

    def delete_task(self, rowid):
        with self.connection:
            return self.cursor.execute('DELETE FROM "tasks" WHERE rowid = ?', (rowid,))

    def delete_task_2(self, symbol, target_price):
        with self.connection:
            return self.cursor.execute(
                'DELETE FROM "tasks" WHERE symbol = ? AND target_price = ?',
                (
                    symbol,
                    target_price,
                ),
            )

    def get_all_tasks(self):
        with self.connection:
            self.cursor.execute('SELECT rowid, symbol, target_price FROM "tasks"')
            return self.cursor.fetchall()
