class Cell:
    def __init__(self, qty):
        self.qty = qty
        if type(qty) != int:
            raise ValueError('Кол-во клеток не является целым числом')

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        diff = Cell(self.qty - other.qty)
        if self.qty - other.qty >= 0:
            return diff
        else:
            print('Разность количества ячеек двух клеток меньше нуля')

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __floordiv__(self, other):
        return Cell(self.qty // other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)

    def make_order(self, n):
        for i in range(self.qty // n):
            print('*' * n)
        print('*' * (self.qty % n))


cell_1 = Cell(12)
cell_2 = Cell(24)
cell_3 = Cell(9)
print((cell_1 + cell_2).qty)
print(cell_1 - cell_2)
print((cell_1 - cell_3).qty)
print((cell_1 * cell_2).qty)
print((cell_1 / cell_2).qty)
print((cell_1 / cell_3).qty)
print((cell_1 // cell_2).qty)
print((cell_1 / cell_3).qty)
cell_1.make_order(10)
