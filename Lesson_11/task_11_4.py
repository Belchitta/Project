class Warehouse:
    """Класс, описывающий склад"""


class OfficeEquipment(Warehouse):
    def __init__(self, voltage='220V', connector="usb"):
        self.voltage = voltage
        self.connector = connector


class Printer(OfficeEquipment):
    def __init__(self, colour='grey', power='300вт'):
        self.colour = colour
        self.power = power


class Scaner(OfficeEquipment):
    def __init__(self, colour='white', power='250вт'):
        self.colour = colour
        self.power = power


class Xerox(OfficeEquipment):
    def __init__(self, colour='black', power='500вт'):
        self.colour = colour
        self.power = power
