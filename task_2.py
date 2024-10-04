class Car:
    def init(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")


class TownCar(Car):
    def init(self, speed, color, name):
        super().init(speed, color, name, is_police=False)

class SportCar(Car):
    def init(self, speed, color, name):
        super().init(speed, color, name, is_police=False)

class WorkCar(Car):
    def init(self, speed, color, name):
        super().init(speed, color, name, is_police=False)

class PoliceCar(Car):
    def init(self, speed, color, name):
        super().init(speed, color, name, is_police=True)