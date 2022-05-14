import itertools
# Первый случай из методички, тут tutors короче, поэтому нет смысла в zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
gen_list = (item for item in zip(tutors, klasses))
print(type(gen_list))
print(*gen_list)
# Самовольно расширила tutors и написала генератор, где как раз удобно применить zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Антон', 'Аркадий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
from itertools import zip_longest

new_list = (item for item in zip_longest(tutors, klasses, fillvalue=None))
print(type(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))