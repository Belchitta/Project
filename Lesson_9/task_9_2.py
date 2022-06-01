class Road:
    __length = 100
    __width = 4

    def road_calc(self, mass, long):
        self.killo = mass
        self.longest = long
        result = (Road.__length * Road.__width * mass * long) / 1000
        print(f'Нужно асфальта: {result} т')


r = Road()
r.road_calc(100, 4)
