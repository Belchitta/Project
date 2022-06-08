class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 'a + b * j'

    def __add__(self, other):
        print(f'Сумма комплексных чисел: ')
        return f'z = {self.x + other.x} + {self.y + other.y} * j'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел: ')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.x * other.y + other.x * self.y} * j'

    def __str__(self):
        return f'z = {self.x} + {self.y} * j'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1, z_2, sep='\n')
print(z_1+z_2)
print(z_1*z_2)

# проверяю себя через complex()
# ==========================>>>

z1 = complex(1, -2)
z2 = complex(3, 4)
print(z1, z2, sep='\n')
print(z1+z2)
print(z1*z2)