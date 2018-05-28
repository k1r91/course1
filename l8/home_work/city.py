import os
import gzip
import json
import urllib.request
from db import Db


class City:

    table_name = 'city'

    def __init__(self, db):
        self.conn = db.conn
        self.unpacked_path_name = os.path.join(os.getcwd(), 'data', 'citi_list.json')
        self.initialize_table()

    def download_cities(self):
        url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        path_name = os.path.join(os.getcwd(), 'data', 'citi_list.json.gz')
        urllib.request.urlretrieve(url, path_name)
        with open(self.unpacked_path_name, 'wb') as f:
            data = gzip.open(path_name)
            f.write(data.read())

    def initialize_table(self, table_name='city'):
        query = '''DROP TABLE IF EXISTS {}'''.format(table_name)
        self.conn.cursor().execute(query)
        query = '''CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY,
                city VARCHAR(255) NOT NULL,
                country VARCHAR(10) NOT NULL,
                lon INTEGER NOT NULL,
                lat INTEGER NOT NULL)
                '''.format(table_name)
        self.conn.cursor().execute(query)

    def load_cities_to_db(self):
        with open(self.unpacked_path_name, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            values = []
            for item in data:
                values.append([
                    item['id'],
                    item['name'],
                    item['country'],
                    item['coord']['lon'],
                    item['coord']['lat']
                ])
            self.conn.executemany('INSERT INTO {} VALUES (?,?,?,?,?)'.format(self.table_name), values)
            self.conn.commit()

    def refresh_cities(self):
        self.download_cities()
        self.load_cities_to_db()


def main():
    # city = City(Db())
    # city.load_cities_to_db()
    pass


if __name__ == '__main__':
    main()