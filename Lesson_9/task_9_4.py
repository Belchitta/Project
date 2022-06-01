class Car:
    def __init__(self, colour, name, speed, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print(self.colour, self.name, 'поехала')

    def stop_car(self):
        print(self.colour, self.name, 'остановилась')

    def go_right(self):
        print(self.colour, self.name, 'повернула направо')

    def go_left(self):
        print(self.colour, self.name, 'повернула налево')

    def show_speed(self):
        print('Текущая скорость автомобиля = ', self.speed)


class TownCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)

    def show_speed(self):
        if self.speed <= 60:
            print('Текущая скорость автомобиля = ', self.speed)
        else:
            print('Превышена допустимая скорость')


class SportCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)


class WorkCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)

    def show_speed(self):
        if self.speed <= 40:
            print('Текущая скорость автомобиля = ', self.speed)
        else:
            print('Превышена допустимая скорость')


class PoliceCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed, True)


car_1 = Car('Серебристый', 'Lexus', 120)
tow_car = TownCar('Голубой', 'Bentley', 59)
sp_car = SportCar('Желтый', 'Porsche Cayman', 180)
w_car = WorkCar('Оранжевый', 'Kamaz', 40)
p_car = PoliceCar('Малиновая', 'Lada', 35)
print(f'Цвет: {car_1.colour}, модель: {car_1.name}, Полицейская: {car_1.is_police}')
car_1.go_car(), car_1.stop_car(), car_1.go_left(), car_1.go_right(), car_1.show_speed()
print(f'Цвет: {tow_car.colour}, модель: {tow_car.name}, Полицейская: {tow_car.is_police}')
tow_car.go_car(), tow_car.stop_car(), tow_car.go_left(), tow_car.go_right(), tow_car.show_speed()
print(f'Цвет: {sp_car.colour}, модель: {sp_car.name}, Полицейская: {sp_car.is_police}')
sp_car.go_car(), sp_car.stop_car(), sp_car.go_left(), sp_car.go_right(), sp_car.show_speed()
print(f'Цвет: {w_car.colour}, модель: {w_car.name}, Полицейская: {w_car.is_police}')
w_car.go_car(), w_car.stop_car(), w_car.go_left(), w_car.go_right(), w_car.show_speed()
print(f'Цвет: {p_car.colour}, модель: {p_car.name}, Полицейская: {p_car.is_police}')
p_car.go_car(), p_car.stop_car(), p_car.go_left(), p_car.go_right(), p_car.show_speed()
sp_car.stop_car()
w = WorkCar('Оранжевый', 'Kamaz', 65)
w.show_speed()
t = TownCar('Голубой', 'Bentley', 120)
t.show_speed()