import os
import sqlite3
import csv
DB_NAME = 'weather.db'


class Db:
    def __init__(self, db_name=DB_NAME):
        self.path_name = os.path.join(os.path.dirname(__file__), 'data')
        try:
            os.mkdir(self.path_name)
        except FileExistsError:
            pass
        self.conn = sqlite3.connect(os.path.join(self.path_name, db_name))

    def close(self):
        self.conn.close()