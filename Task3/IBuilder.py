from abc import ABC, abstractmethod


class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def setSeats(self) -> None:
        pass

    @abstractmethod
    def setEngine(self) -> None:
        pass

    @abstractmethod
    def setTripComputer(self) -> None:
        pass

    @abstractmethod
    def setGPS(self) -> None:
        pass
