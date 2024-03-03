def finish_him(func):

    def wrapper(*smth):
        result = func(*smth)
        print('finished')
        return result
    return wrapper


@finish_him
def scorpion():
    print('Get over here!')
    print('--------------->')


scorpion()
