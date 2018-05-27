import urllib.request
import json
import datetime
from db import Db
from city import City


class WeatherRequest:
    table_name = 'weather_data'

    def __init__(self, db):
        self.conn = db.conn
        self.initialize_table()
        self.app_id = self.get_app_id()

    def initialize_table(self):
        # self.conn.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))
        query = '''CREATE TABLE IF NOT EXISTS {} (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER NOT NULL,
        current_date DATE NOT NULL,
        temperature INTEGER NOT NULL,
        FOREIGN KEY(id) REFERENCES {}(id))'''.format(self.table_name, City.table_name)
        self.conn.execute(query)

    @staticmethod
    def get_app_id():
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
        self.save(request_data)
        return request_data

    def request_by_country(self, country, metric='metric'):
        '''
        performs request to group of cities
        :param country: 
        :param metric: 
        :return: 
        '''
        query = 'SELECT id FROM {} WHERE country = "{}"'.format(City.table_name, country)
        cities = self.conn.execute(query).fetchall()
        if not cities:
            return "This country does not exists"
        cities = [str(city[0]) for city in cities]
        data = []
        for city in cities:
            request_url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units={}&appid={}'.format(
                city,
                metric,
                self.app_id, )
            request_data = json.load(urllib.request.urlopen(request_url))
            data.append(request_data)
        return data

    def save(self, data):
        current_date = str(datetime.datetime.now())
        city_id = data['id']
        temperature = data['main']['temp']
        query = 'INSERT INTO {} (city_id, current_date, temperature) VALUES({}, "{}", {})'.format(
            self.table_name, city_id, current_date, temperature)
        self.conn.execute(query)
        self.conn.commit()

    def test_save(self):
        query = 'INSERT INTO {} (city_id, current_date, temperature) VALUES({}, "{}", {})'.format(
            self.table_name,
            707860,
            datetime.datetime.now(),
            25
        )
        self.conn.execute(query)
        self.conn.commit()


def main():
    weather = WeatherRequest(Db())
    print(weather.request('Yekaterinburg'))
    # print(weather.request_by_country('RU'))


if __name__ == '__main__':
    main()
