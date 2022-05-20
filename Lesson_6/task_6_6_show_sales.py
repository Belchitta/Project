import sys


def sale(argv):
    program, *args = argv
    if comand == 0:
        with open('bakery.csv', 'r', encoding='utf-8') as b:
            for line in b:
                print(line.strip('\n'))
    elif comand == 1:
        numb = int(input('Введите число '))
        with open('bakery.csv', 'r', encoding='utf-8') as b:
            for line in range(0, numb):
                print(b.readline().strip('\n'))
            if numb == 0:
                print(b.readline().strip('\n'))
    elif comand == 2:
        start = int(input('Введите число c '))
        end = int(input('Введите число по '))
        with open('bakery.csv', 'r', encoding='utf-8') as b:
            for line in range(start, end + 1):
                print(b.readline().strip('\n'))


comand = int(input('''Введите параметр запуска:
- 0:показать список,
- 1: показать зданное кол-во продаж,
- 2: показать кол-во продаж с _по_ = введенным числам
---'''))


if __name__ == '__main__':
    import sys
    print(sys.argv)
    sale(sys.argv)
