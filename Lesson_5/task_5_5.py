# Ниже привожу два решения с измерениями: первое «в лоб со списком», второе – обернув
# решение из методички в функцию.
# Исходя из времени выполнения получается, что простое решение со списком выполняется быстрее.
# А раз памяти они занимают одинаково, логично использовать более быстрое.
import sys
from time import perf_counter
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
src_uniq = []
for item in src:
    if item not in src_uniq:
        src_uniq.append(item)
    else:
        src_uniq.remove(item)
print(type(src_uniq), sys.getsizeof(src_uniq), src_uniq, perf_counter() - start)



def uniq_numb(src):
    uni_numb = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            uni_numb.add(el)
        else:
            uni_numb.discard(el)
        tmp.add(el)
    unique_numbers_ord = [el for el in src if el in uni_numb]
    return unique_numbers_ord

start = perf_counter()
uniq_numb(src)
print(type(uniq_numb(src)), sys.getsizeof(uniq_numb(src)), uniq_numb(src), perf_counter() - start)
