import collections

from datetime import datetime
from colorama import init, Fore, Style
init()
err_len = 300
txt_wrap = 150


def get_datetime(line):
    try:
        date = line[:line.find(' ', line.find(' ') + 1)]
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        return date
    except ValueError:
        return False


def get_log(line):
    if get_datetime(line):
        return line[line.find(' ', line.find(' ') + 1) + 1:]


def make_me_dict(file, logs):
    with open(file, newline='') as curr_file:
        for line in curr_file:
            if get_datetime(line):
                key = get_datetime(line)
                logs[key] = get_log(line)
            else:
                logs[key] += line
    return logs


def date_search(logs, date, result_logs=collections.defaultdict()):
    # Cтрогое сравнение по дате
    if date.find('/') == -1 and date.find('..') == -1:
        req_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        if req_datetime in logs.keys():
            result_logs = {req_datetime: logs[req_datetime]}
            return result_logs
        else:
            print(f'No logs for {req_datetime}')
    # Позже указанной даты
    elif date.find('/') < date.find('..'):
        req_datetime = datetime.strptime(date[:-3], '%Y-%m-%d %H:%M:%S.%f')
        result_logs = dict(filter(lambda item: item[0] > req_datetime, logs.items()))
        # result_logs = {date: logs[date] for date in result}
        return result_logs
    # Раньше указанной даты
    elif date.find('/') > date.find('..') and date.find('..') != -1:
        req_datetime = datetime.strptime(date[3:], '%Y-%m-%d %H:%M:%S.%f')
        result_logs = dict(filter(lambda item: item[0] < req_datetime, logs.items()))
        # result_logs = {date: logs[date] for date in result}
        return result_logs
    # Между двумя датами
    elif date.find('/') > date.find('..') and date.find('..') == -1:
        start_date = datetime.strptime(date[:date.find('/')], '%Y-%m-%d %H:%M:%S.%f')
        end_date = datetime.strptime(date[date.find('/') + 1:], '%Y-%m-%d %H:%M:%S.%f')
        result_logs = dict(filter(lambda item: (item[0] > start_date and item[0] < end_date), logs.items()))
        # result_logs = {date: logs[date] for date in result}
        return result_logs


def text_search(logs, text='', notext=''):
    # Есть только text
    if bool(text) and not bool(notext):
        result_logs = dict(filter(lambda item: text in item[1], logs.items()))
    # Есть text и notext
    if bool(text) and bool(notext):
        result_logs = dict(filter(lambda item: (text in item[1] and notext not in item[1]), logs.items()))
    # Есть только notext
    if not bool(text) and bool(notext):
        result_logs = dict(filter(lambda item: notext not in item[1], logs.items()))
    return result_logs


def printer(result_logs, full=False, text=''):
    # При поиске по тексту - берём кусок с обеих сторон от текста
    if bool(text):
        for key, value in result_logs.items():
            text_ind = value.find(text)
            start_text = value[:text_ind] if len(value[:text_ind]) < 150 else value[text_ind-150:text_ind]
            end_text = value[text_ind:] if len(value[text_ind:]) < 150 else value[text_ind:text_ind+150]
            print(Fore.YELLOW, key, Style.RESET_ALL, start_text+end_text)
    # Был запрошен полный текст ошибки
    elif full:
        for key, value in result_logs.items():
            print(Fore.YELLOW, key, Style.RESET_ALL, value)
    # По умолчанию берём срез до 300 символов, наверное основной кейс должен быть верхним :)
    else:
        for key, value in result_logs.items():
            print(Fore.YELLOW, key, Style.RESET_ALL, value[:err_len] if len(value) > err_len else value)
