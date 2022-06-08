import re


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, data):
        d = data.split("-")
        for i in d:
            i = int(i)
        date = d
        return date

    @staticmethod
    def valid_data(date):
        corr_date = re.compile(r'^(\d{2}.){2}\d{4}$')
        assert corr_date.match(date), f'wrong date {date}'
        d = date.split("-")
        if int(d[1]) < 13:
            print('OK')
        else:
            raise ValueError('Дата некорректна')


s = Data('05-07-2022')
print(s.extract('05-12-2022'))
s.valid_data('05-07-2022')
