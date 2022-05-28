import re


def email_parse(mail):
    try:
        result = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", mail)
        if result:
            result_= re.split('@', mail)
            dict_result = {'username': result_[0], 'domain': result_[1]}
            print(dict_result)
        else:
            raise ValueError(f'wrong email: {mail}')
    except ValueError:
        print(f'wrong email: {mail}')


email_parse('someone@geekbrains.ru')

