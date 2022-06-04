m_1 = [[31, 22], [37, 43], [51, 86]]
m_2 = [[9, 8], [3, 7], [9, 4]]

class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return '\n'.join(str(i) for i in self.args)

    def __add__(self, other):
        return Matrix([x + y for x, y in zip(list_1, other_list)] for list_1, other_list in zip(self.args, other.args))

first_matrix = Matrix(m_1)
print(first_matrix, '\n')
second_matrix = Matrix(m_2)
print(second_matrix, '\n')
third_matrix = first_matrix + second_matrix
print(third_matrix, '\n')


