import os
parent_dir = 'my_project'
child_dir = 'settings', 'mainapp', 'adminapp', 'authapp'
try:
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)
        for item in child_dir:
            dir_path = os.path.join(parent_dir, item)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
except FileExistsError:
    print('Папка уже существует')