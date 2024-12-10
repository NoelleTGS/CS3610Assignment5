from Builder import Builder


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def makeSportsCar(self):
        self.builder.reset()
        self.builder.setType("Sports Car")
        self.builder.setSeats(2)
        self.builder.setEngine("V8")
        self.builder.setGPS(True)

    def makeSUV(self):
        self.builder.reset()
        self.builder.setType("SUV")
        self.builder.setSeats(5)
        self.builder.setEngine("V6")
        self.builder.setGPS(False)