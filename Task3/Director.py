from typing import Type

from Task3 import IBuilder


class Director:
    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self) -> IBuilder:
        return self.__builder

    @builder.setter
    def builder(self, builder: Type[IBuilder]) -> None:
        self.__builder = builder

    def makeSUV(self) -> None:
        pass

    def makeSportsCar(self) -> None:
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(SportEngine())
        builder.setTripComputer()
        builder.setGPS()