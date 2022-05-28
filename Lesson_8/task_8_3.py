numbers = dict(one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
               eight='восемь', nine='девять', ten='десять')


def type_logger(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(type(*args, **kwargs))
        # Ниже закоментила ответ на 'Сможете ли вывести имя функции, например, в виде: calc_cube(5: <class 'int'>):
        # print(func.__name__, *args, type(*args, **kwargs))

    return wrapper


@type_logger
def num_translate(number):
    """Convert numbers from english to russian"""
    number = numbers.get(number)
    print(number)


num_translate('one')