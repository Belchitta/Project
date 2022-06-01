class Stationery:
    title = 'Инструмент'

    def draw(self):
        print('Запуск отрисовки', self.title)


class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print('Рисуем ручкой, инструмент:', self.title)


class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print('Рисуем карандашом, инструмент:', self.title)


class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print('Рисуем тонкой ручкой, инструмент:', self.title)

st_1 = Stationery()
st_2 = Pen()
st_3 = Pencil()
st_4 = Handle()
st_1.draw(), st_2.draw(), st_3.draw(), st_4.draw()