# Zadanie 3
# Zaimplementuj klasę ElectricCar odwzorowującą zachowanie
# samochodu elektrycznego. Klasa powinna umożliwiać pokonanie zadanego dystansu,
# który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla
# samochodu. Samochód powinien mieć także możliwość naładowania baterii.

class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self._distance_traveled = 0

    def drive(self, distance):
        "Zwraca ile kilometrów przejedzie"
        if distance + self._distance_traveled > self.max_range:
            to_drive = self.max_range - self._distance_traveled
            self._distance_traveled = self.max_range
        else:
            to_drive = distance
            self._distance_traveled += distance

        print(to_drive)
        return to_drive


    def charge(self):
        self._distance_traveled = 0

car = ElectricCar(100)

car.drive(30)
car.drive(50)
car.drive(30)
car.drive(10)
car.charge()
car.drive(190)

