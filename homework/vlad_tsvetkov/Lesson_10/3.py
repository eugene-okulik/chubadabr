def operation_teller(func):
    def wrapper(num1, num2):
        if num1 == num2:
            print(func(num1, num2, '+'))
        elif num1 > num2:
            print(func(num1, num2, '-'))
        elif num1 < num2:
            print(func(num1, num2, '/'))
        elif num1 < 0 or num2 < 0:
            print(func(num1, num2, '*'))
    return wrapper


@operation_teller
def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        return num1 / num2
    elif operation == '*':
        return num1 * num2


num1, num2 = [float(_) for _ in input('Введите два числа через пробел ').split()]
calc(num1, num2)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
new_list = list(el.split() for el in PRICE_LIST.split('\n'))
for el in new_list:
    el[1] = int(el[1][:-1])
print(dict(new_list))
