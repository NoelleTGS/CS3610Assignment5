from Builder import Builder
from Car import Car

# Concrete Builder for Car
class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def setType(self, type: str):
        self.car.type = type

    def setSeats(self, seats: int):
        self.car.seats = seats

    def setEngine(self, engine: str):
        self.car.engine = engine

    def setGPS(self, gps: bool):
        self.car.gps = gps

    def getResult(self):
        return self.car
