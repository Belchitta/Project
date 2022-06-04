from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def clothes_qt(self):
        pass


class Coat(Clothes):
    @property
    def clothes_qt(self):
        v = self.param / 6.5 + 0.5
        return v


class Suit(Clothes):
    @property
    def clothes_qt(self):
        h = 2 * self.param + 0.3
        return h


m = Suit(1.82)
f = Coat(42)
print(m.clothes_qt, f.clothes_qt, sep='\n')
# это если по заданию нужно было посчитать сумму ткани на пальто и костюм
print(m.clothes_qt + f.clothes_qt)
