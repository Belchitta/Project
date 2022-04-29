# 2
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_list.pop(1)
some_list.pop(-2)
some_list.pop(2)
some_list.insert(1, '"05"')
some_list.insert(-1, '"+05"')
some_list.insert(3, '"17"')

print(' '.join(some_list))
