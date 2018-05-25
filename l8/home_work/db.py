import os
import sqlite3
DB_NAME = 'weather.db'


class Db:
    def __init__(self, db_name=DB_NAME):
        path_name = os.path.join(os.getcwd(), 'data')
        try:
            os.mkdir(path_name)
        except FileExistsError:
            pass
        self.conn = sqlite3.connect(os.path.join(path_name, db_name))

    def close(self):
        self.conn.close()