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
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.brand} {self.model} {self.colour} {self.power}'


class Printer(OfficeEquipment):
    def __init__(self, name, brand, model, colour, power):
        super().__init__(name, brand)
        self.model = model
        self.colour = colour
        self.power = power


class Scaner(OfficeEquipment):
    def __init__(self, name, brand, model, colour, power):
        super().__init__(name, brand)
        self.model = model
        self.colour = colour
        self.power = power


class Xerox(OfficeEquipment):
    def __init__(self, name, brand, model, colour, power):
        super().__init__(name, brand)
        self.model = model
        self.colour = colour
        self.power = power


tech = Warehouse()
printer = Printer('Принтер', 'Kyocera', '1510', 'белый', '300Вт')
tech.add_tech(printer)
printer_ = Printer('Принтер', 'Kyocera', '4410', 'серый', '300Вт')
tech.add_tech(printer_)
scaner = Scaner('Сканер', 'HP', '5070', 'серый', '250Вт')
tech.add_tech(scaner)
xerox = Xerox('Ксерокс', 'Canon', '3510', 'черный', '400Вт')
tech.add_tech(xerox)
print(tech._dict)
tech.removal('Printer')
print()
print(tech._dict)