def val_sqrt(x=2):
    def sqrt(func):
        def sqrt_numbers(arg):
            try:
                if arg == int(arg):
                    func(arg)
                    result = arg ** x
                    print(f'Результат вычислений = {result}, значение x = {x}')
                    return result
            except ValueError:
                print('Неверное значение для вычисления')
        return sqrt_numbers
    return sqrt


@val_sqrt(x=1)
def sqrt_numbers(arg):
    x = 2
    result = arg ** x
    return result


print(sqrt_numbers(5))