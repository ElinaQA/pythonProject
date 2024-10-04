class TownCar:
    def __init__(self, speed, color, name):
        self.speed = speed        # Скорость
        self.color = color        # Цвет
        self.name = name          # Название модели
        self.is_police = False    # Полицейская ли это машина

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")


class SportCar:
    def __init__(self, speed, color, name):
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
    def __init__(self, speed, color, name):
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
    def __init__(self, speed, color, name):
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


town_car = TownCar(60, "Синий", "Городская машина")
sport_car = SportCar(150, "Красный", "Спортивная машина")
work_car = WorkCar(40, "Белый", "Рабочая машина")
police_car = PoliceCar(100, "Чёрный", "Полицейская машина")

town_car.go()
town_car.turn("налево")
town_car.stop()

police_car.go()
police_car.turn("направо")
police_car.stop()