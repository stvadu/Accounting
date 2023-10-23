import datetime
from pprint import pprint

from application.db.people import get_employees
from application.salary import calculate_salary

from google_trends import realtime_trends

if __name__ == '__main__':
    start = datetime.datetime.now()
    print(f'список сотрудников: {get_employees("db.txt")}')
    print(f'вся зарплата: {calculate_salary(50000, "db.txt")}')
    time_count = datetime.datetime.now() - start
    print(f'Done with {time_count}')
    print('А теперь немного ерунды из мира спорта:')
    pprint(realtime_trends(country='RU', language='ru-RU', category='s', num_results=5, timezone='-180'))