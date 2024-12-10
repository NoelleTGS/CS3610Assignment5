from abc import ABC, abstractmethod

# Abstract Builder Interface
class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setType(self, type_: str):
        pass

    @abstractmethod
    def setSeats(self, seats: int):
        pass

    @abstractmethod
    def setEngine(self, engine: str):
        pass

    @abstractmethod
    def setGPS(self, gps: bool):
        pass