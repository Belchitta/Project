def odd_nums_gen(n):
    for i in range(1, n + 1, 2):
        yield i


num = odd_nums_gen(4)
print(next(num))
print(next(num))
print(next(num))
