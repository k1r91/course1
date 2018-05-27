import os
import sys
import csv
import json
from db import Db
from weather import WeatherRequest
from city import City

DEFAULT_PATH = os.path.dirname(__file__)


def export(func, path=DEFAULT_PATH):
    db = Db()
    conn = db.conn
    query = 'SELECT * FROM {} INNER JOIN {} ON {}.city_id = {}.id'.format(WeatherRequest.table_name,
                                                                     City.table_name,
                                                                     WeatherRequest.table_name,
                                                                     City.table_name)
    data = conn.execute(query).fetchall()
    with open(path, 'w', encoding='utf-8') as file:
        try:
            func(data, file)
        except FileNotFoundError:
            print('Directory does not exist.')
    print('Database was exported to {}'.format(path))


def export_csv(data, file):
    writer = csv.writer(file, delimiter=';')
    for row in data:
        writer.writerow(row)


def export_json(data, file):
    file.write(json.dumps(data))


def export_html(data, file):
    html = '<html><body><table>{}'.format(os.linesep)
    for row in data:
        html = ''.join([html, '<tr>{}'.format(os.linesep)])
        for item in row:
            html = ''.join([html, '<td>{}'.format(item)])
            html = ''.join([html, '</td>'.format(os.linesep)])
        html = ''.join([html, '</tr>{}'.format(os.linesep)])
    html = ''.join([html, '</table></html></body>'])
    file.write(html)


if __name__ == '__main__':
    args = ['csv', 'json', 'html']
    try:
        arg = sys.argv[1][2:]
        path_to_file = sys.argv[2]
        if arg not in args:
            print('Possible arguments: csv, json, html')
            sys.exit(1)
    except IndexError:
        print('Usage: python export_db.py --[option] [path_to_file]')

    if arg == 'csv':
        export(export_csv, path_to_file)
    elif arg == 'json':
        export(export_json, path_to_file)
    else:
        export(export_html, path_to_file)
