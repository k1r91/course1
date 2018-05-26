import os
from db import Db
from weather import WeatherRequest
from city import City


def export_csv(path):
    db = Db()
    print(os.path.dirname(__file__))
    conn = db.conn
    query = 'SELECT * FROM {} INNER JOIN {} ON {}.city_id = {}.id'.format(WeatherRequest.table_name,
                                                                     City.table_name,
                                                                     WeatherRequest.table_name,
                                                                     City.table_name)
    print(query)
    print(conn.execute(query).fetchall())


if __name__ == '__main__':
    export_csv(os.path.join('data', 'weather.csv'))
