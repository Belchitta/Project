import json
users = ['Иванов,Иван,Иванович,\nПетров,Петр,Петрович,\nСидоров,Иоган,Владимирович,\nПетрова,Элеонора,Петровна']
hobby = ['скалолазание,\nохота,\nгорные лыжи']
dict_person_hobbie = {}
with open('users.csv', 'w', encoding='utf-8') as f:
    f.writelines(users)
with open('hobby.csv', 'w', encoding='utf-8') as f:
    f.writelines(hobby)
with open('users.csv', 'r', encoding='utf-8') as f:
    line_users = f.readlines()
    clean_line_user = map(lambda s: s.strip(',\n'), line_users)
    clean_line_users = [*clean_line_user]
with open('hobby.csv', 'r', encoding='utf-8') as f:
        line_hobbies = f.readlines()
        clean_line_hobbie = map(lambda s: s.strip(',\n'), line_hobbies)
        clean_line_hobbies = [*clean_line_hobbie]
for i in range(len(clean_line_users)):
    if len(clean_line_hobbies) > len(clean_line_users):
        print('выходим из скрипта с кодом «1».')
        break
    if len(clean_line_hobbies) < len(clean_line_users):
        clean_line_hobbies.append(None)
    dict_person_hobbie[clean_line_users[i]] = clean_line_hobbies[i]
print(dict_person_hobbie)


with open('dict_person_hobbie','w', encoding='utf-8') as d:
    json.dump(dict_person_hobbie, d)
with open('dict_person_hobbie','r', encoding='utf-8') as m:
    d = json.load(m)
    print(d)

