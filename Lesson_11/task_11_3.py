class Verifyrightnums(Exception):
    """Проверяет содержимое списка на наличие только чисел"""


list_args = []
while True:
    try:
        num = input('Введите число или "stop": ')
        if num == 'Stop':
            break
        if not num.isdigit():
            raise Verifyrightnums
        list_args.append(int(num))
    except Verifyrightnums:
        print('Значение не число')
print(list_args)
