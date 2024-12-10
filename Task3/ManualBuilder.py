from Builder import Builder
from Manual import Manual

# Concrete Builder for Manual
class ManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def setType(self, type: str):
        self.manual.type = type

    def setSeats(self, seats: int):
        self.manual.instructions += f"Car has {seats} seats.\n"

    def setEngine(self, engine: str):
        self.manual.instructions += f"Engine: {engine}.\n"

    def setGPS(self, gps: bool):
        self.manual.instructions += f"GPS: {'Included' if gps else 'Not included'}.\n"

    def getResult(self):
        return self.manual