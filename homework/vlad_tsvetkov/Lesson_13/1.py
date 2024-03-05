import os
import datetime

file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
dates_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')
weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}


def get_date(text):
    date = text[3:line.index(' - ')]
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    return date


def get_line_num(text):
    return int(text[:text.index('.')])


with open(dates_path, 'r') as dates_data:
    for line in dates_data.readlines():
        date = get_date(line)
        if get_line_num(line) == 1:
            print(date + datetime.timedelta(days=7))
        elif get_line_num(line) == 2:
            print(weekdays[datetime.datetime.weekday(date)])
        elif get_line_num(line) == 3:
            date_diff = datetime.datetime.now() - date
            print(date_diff.days)
        else:
            print('Моя не понимать такое')
