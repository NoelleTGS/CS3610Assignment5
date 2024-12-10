
class Car:
    def __init__(self):
        self.type = None
        self.seats = None
        self.engine = None
        self.gps = None

    def __str__(self):
        return (
            f"Car type: {self.type}, Seats: {self.seats}, "
            f"Engine: {self.engine}, GPS: {self.gps}"
        )