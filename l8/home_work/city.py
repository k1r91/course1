import os
import gzip
import json
import urllib.request
from db import Db


class City:

    table_name = 'city'

    def __init__(self, db):
        self.db = db
        self.conn = db.conn
        self.unpacked_path_name = os.path.join(os.getcwd(), 'data', 'citi_list.json')
        self.initialize_db()

    def download_cities(self):
        url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        path_name = os.path.join(os.getcwd(), 'data', 'citi_list.json.gz')
        if not os.path.exists(path_name):
            urllib.request.urlretrieve(url, path_name)
        if not os.path.exists(self.unpacked_path_name):
            with open(self.unpacked_path_name, 'wb') as f:
                data = gzip.open(path_name)
                f.write(data.read())

    def initialize_db(self, table_name='city'):
        query = '''DROP TABLE {}'''.format(table_name)
        self.conn.cursor().execute(query)
        query = '''CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY,
                city VARCHAR(255) NOT NULL,
                coord VARCHAR(255) NOT NULL,
                date_request DATE NOT NULL,
                temp INTEGER NOT NULL,
                weather_id INTEGER NOT NULL)
                '''.format(table_name)
        self.conn.cursor().execute(query)

    def load_cities_to_db(self):
        with open(self.unpacked_path_name, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            for item in data:
                print(item)
                id_k = item['id']


def main():
    city = City(Db())
    city.download_cities()
    city.load_cities_to_db()


if __name__ == '__main__':
    main()