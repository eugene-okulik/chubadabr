s1 = 'результат операции: 42'
s2 = 'результат операции: 54'
s3 = 'результат работы программы: 209'
s4 = 'результат: 2'


def summer(s: str):
    print(int(s.split()[-1]) + 10)


summer(s1)
summer(s2)
summer(s3)
summer(s4)
