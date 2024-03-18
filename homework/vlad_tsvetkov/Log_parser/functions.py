import collections

from datetime import datetime
from colorama import init, Fore, Style
init()


def is_datetime(line):
    try:
        date = line[:line.find(' ', line.find(' ')+1)]
        datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        return True
    except ValueError:
        return False


def get_datetime(line):
    date = datetime.strptime(line[:line.find(' ', line.find(' ')+1)],  '%Y-%m-%d %H:%M:%S.%f')
    return date


def get_log(line):
    if is_datetime(line):
        return line[line.find(' ', line.find(' ')+1)+1:]


def make_me_dict(file, logs):
    with open(file, newline='') as curr_file:
        for line in curr_file:
            if is_datetime(line):
                key = get_datetime(line)
                logs[key] = get_log(line)
            else:
                logs[key] += line
    return logs


def date_search(logs, date):
    result_logs = collections.defaultdict()
    if date.find('/') == -1 and date.find('..') == -1:
        req_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        if req_datetime in logs.keys():
            print(Fore.YELLOW, req_datetime, Style.RESET_ALL, logs[req_datetime][:300])
            print(Fore.GREEN)
            answer = input("Wanna get full message? y/n ")
            print(Style.RESET_ALL)
            if answer == 'y':
                print(Fore.YELLOW, req_datetime, Style.RESET_ALL, logs[req_datetime])
        else:
            print(f'No logs for {req_datetime}')
    elif date.find('/') < date.find('..'):
        req_datetime = datetime.strptime(date[:-3], '%Y-%m-%d %H:%M:%S.%f')
        result = list(filter(lambda key: key > req_datetime, logs.keys()))
        result_logs = {date: logs[date] for date in result}
        for key, value in result_logs.items():
            print(Fore.YELLOW, key, Style.RESET_ALL, value[:300] if len(value) > 300 else value)
    elif date.find('/') > date.find('..') and date.find('..') != -1:
        req_datetime = datetime.strptime(date[3:], '%Y-%m-%d %H:%M:%S.%f')
        result = list(filter(lambda key: key < req_datetime, logs.keys()))
        result_logs = {date: logs[date] for date in result}
        for key, value in result_logs.items():
            print(Fore.YELLOW, key, Style.RESET_ALL, value[:300] if len(value) > 300 else value)
    elif date.find('/') > date.find('..') and date.find('..') == -1:
        start_date = datetime.strptime(date[:date.find('/')], '%Y-%m-%d %H:%M:%S.%f')
        end_date = datetime.strptime(date[date.find('/')+1:], '%Y-%m-%d %H:%M:%S.%f')
        result = list(filter(lambda key: (key > start_date and key < end_date), logs.keys()))
        result_logs = {date: logs[date] for date in result}
        for key, value in result_logs.items():
            print(Fore.YELLOW, key, Style.RESET_ALL, value[:300] if len(value) > 300 else value)


def text_search(logs, text, notext=False):
    # result_logs = collections.defaultdict()
    for key, value in logs.items():
        if value.find(text) != -1 and notext is False:
            text_ind = value.find(text)
            start_text = value[:text_ind] if len(value[:text_ind]) < 150 else value[text_ind-150:text_ind]
            end_text = value[text_ind:] if len(value[text_ind:]) < 150 else value[text_ind:text_ind+150]
            print(Fore.YELLOW, key, Style.RESET_ALL, start_text+end_text)
        elif notext is True:
            for key, value in logs.items():
                if text not in value:
                    print(Fore.YELLOW, key, Style.RESET_ALL, value[:300])
