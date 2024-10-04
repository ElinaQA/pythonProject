class TownCar:
    def init(self, speed, color, name):
        self.speed = speed        # Скорость
        self.color = color        # Цвет
        self.name = name          # Название марки модели
        self.is_police = False    # Полицейская ли это машина

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

class SportCar:
    def init(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

class WorkCar:
    def init(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

class PoliceCar:
    def init(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")