import urllib.request
import json
from db import Db
from city import City


class WeatherRequest:
    table_name = 'weather_data'
    def __init__(self, db):
        self.conn = db.conn
        self.initialize_table()
        self.app_id = self.get_app_id()

    def initialize_table(self):
        self.conn.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))
        query = '''CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER NOT NULL,
        current_date DATE NOT NULL,
        temperature INTEGER NOT NULL,
        FOREIGN KEY(id) REFERENCES {}(id))'''.format(self.table_name, City.table_name)
        self.conn.execute(query)

    def get_app_id(self):
        with open('app.id', 'r', encoding='utf-8') as f:
            return f.read().strip()

    def request(self, city, metric='metric'):
        '''
        perform request
        :param city: city name as string
        :param metric: use default to get celsius
        :return: data ready to save in database
        '''
        query = 'SELECT id FROM {} WHERE city = "{}"'.format(City.table_name, city)
        try:
            city_id = self.conn.execute(query).fetchone()[0]
        except TypeError:
            return "This city does not exists"
        request_url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units={}&appid={}'.format(
            city_id,
            metric,
            self.app_id,)
        request_data = json.load(urllib.request.urlopen(request_url))
        return request_data

def main():
    weather = WeatherRequest(Db())
    print(weather.request('Yekaterinburg'))


if __name__ == '__main__':
    main()