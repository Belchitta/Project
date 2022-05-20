import sys


def add_sale(argv):
    program, *args = argv
    data_correct = f'{data}\n'
    with open('bakery.csv', 'a+', encoding='utf-8') as s:
        s.writelines(data_correct)
    print('Сохранено')


data = input('Введите сумму продажи: ')

if __name__ == '__main__':
    import sys
    print(sys.argv)
    add_sale(sys.argv)