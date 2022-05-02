numbers = dict(one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
               eight='восемь', nine='девять', ten='десять')

number = input('Введите число ')


def num_translate(number):
    """Convert numbers from english to russian"""
    print(numbers.get(number))


num_translate(number)
