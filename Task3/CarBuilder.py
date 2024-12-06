from Task3 import IBuilder
from Task3.Car import Car


class CarBuilder(IBuilder):
    def __init__(self) -> None:
        self.__product = None
        self.reset()

    def reset(self) -> None:
        print("We have our initial Product")
        self.__product = Car()

    @property
    def product(self) -> Car:
        currentProduct = self.__product
        self.reset()
        return currentProduct

    def setSeats(self) -> None:
        pass

    def setEngine(self) -> None:
        pass

    def setTripComputer(self) -> None:
        pass

    def setGPS(self) -> None:
        pass
