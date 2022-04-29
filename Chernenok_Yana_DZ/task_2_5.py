# 5
price_list = [5, 10.7, 20.90, 21.05, 17.00, 15.99, 30.05, 31.99, 80.50, 50.50]
# A
for price in price_list:
    print(f"{int(price)} руб. {int(price * 100 % 100):02} коп.", end=', ')
# B
print('\nid price_list', id(price_list))
price_list.sort()
print('\nid price_list', id(price_list), price_list)

# C
price_list_rev = sorted(price_list, reverse=True)
print('\nid price_list', id(price_list_rev), price_list_rev)

# D
print('\nTop 5 price', price_list[-5:])