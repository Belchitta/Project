class Worker:
    name = 'Иван'
    surname = 'Работягов'
    position = 'Стажер'
    __income = {"wage": 20000, "bonus": 10000}


class Position(Worker):
    def __init__(self, name, surname, position):
        self.get_full_name = (f'{surname} {name}, {position}')
        s = Worker
        self.get_total_income = s._Worker__income.get("wage") + s._Worker__income.get('bonus')


a = Position('Сергей', 'Есенин', "писатель")
print(a.get_full_name)
print(a.get_total_income)

