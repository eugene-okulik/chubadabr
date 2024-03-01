import datetime

date = "Jan 15, 2023 - 12:05:33"
py_date = datetime.datetime.strptime(date, '%b %d, %Y - %X')
print(py_date.strftime('%B'))
print(py_date.strftime('%d.%m.%Y, %H:%M'))

temperatures = (
    [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31,
     33, 31, 30, 32, 30, 28, 24, 23])
hot_temps = list(filter(lambda x: x > 28, temperatures))
print(f'Максимальная температура: {max(hot_temps)}')
print(f'Минимальная температура: {min(hot_temps)}')
print(f'Средняя температура: {int(sum(hot_temps) / len(hot_temps))}')
