def decorator_wrapper(num):
    def repeater(func):
        def wrapper(*smth):
            for _ in range(num):
                result = func(*smth)
            return result
        return wrapper

    return repeater


@decorator_wrapper(3)
def printer():
    print('typing smth...')


printer()
