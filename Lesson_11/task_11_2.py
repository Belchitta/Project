class Exceptionzerodivision(Exception):
    """Класс исключения деления на ноль"""


class Division:
    a = 5

    def __init__(self, num):
        self.num = num

    def division_nums(self):
        inp_data = int(self.num)
        try:
            if inp_data == 0:
                raise Exceptionzerodivision('На ноль делить нельзя')
            res = (self.a / inp_data)
            return res
        except Exceptionzerodivision:
            return 'На ноль делить нельзя'


example = Division(0)
print(example.division_nums())
