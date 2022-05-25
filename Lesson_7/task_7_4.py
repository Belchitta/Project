import os
folder = '.'
dict = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        key = 10 ** len(str(size))
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
for key, val in sorted(dict.items()):
    print(f'{key}: {val}')