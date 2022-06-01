import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print('Запуск')
        color_red = 'красный'
        color_yellow = 'желтый'
        color_green = 'зеленый'
        print(color_red)
        time.sleep(7)
        print(color_yellow)
        time.sleep(2)
        print(color_green)
        time.sleep(5)
        print('Finish')


a = TrafficLight()
a.running()
