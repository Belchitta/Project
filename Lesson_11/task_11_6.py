class Warehouse:
    """Класс, описывающий склад"""

    def __init__(self):
        self._dict = {}

    def add_tech(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def removal(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class OfficeEquipment(Warehouse):
    def __init__(self, name, brand, qtty):
        self.name = name
        self.brand = brand
        self.qtty = qtty
        self.group = self.__class__.__name__

    def corrval(self, qtty):
        """механизм валидации вводимого пользователем количества единиц техники """
        self.qtty = int(qtty)
        if type(qtty) != int:
            raise ValueError('Количество должно быть цифрой')

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.brand} {self.model}, количество: {self.qtty}, {self.colour} {self.power}'


class Printer(OfficeEquipment):
    def __init__(self, name, brand, model, qtty, colour, power):
        super().__init__(name, brand, qtty)
        self.model = model
        self.colour = colour
        self.power = power


class Scaner(OfficeEquipment):
    def __init__(self, name, brand, model, qtty, colour, power):
        super().__init__(name, brand, qtty)
        self.model = model
        self.colour = colour
        self.power = power


class Xerox(OfficeEquipment):
    def __init__(self, name, brand, model, qtty, colour, power):
        super().__init__(name, brand, qtty)
        self.model = model
        self.colour = colour
        self.power = power


tech = Warehouse()
printer = Printer('Принтер', 'Kyocera', '1510', 1, 'белый', '300Вт')
printer.corrval(printer.qtty)  # проверка является ли количество числом
tech.add_tech(printer)
printer_ = Printer('Принтер', 'Kyocera', '4410', 2, 'серый', '300Вт')
printer_.corrval(printer_.qtty)
tech.add_tech(printer_)
scaner = Scaner('Сканер', 'HP', '5070', 2, 'серый', '250Вт')
scaner.corrval(scaner.qtty)
tech.add_tech(scaner)
xerox = Xerox('Ксерокс', 'Canon', '3510', 1, 'черный', '400Вт')
xerox.corrval(xerox.qtty)
tech.add_tech(xerox)
print(tech._dict)
tech.removal('Printer')
print()
print(tech._dict)
