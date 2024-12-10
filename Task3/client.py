from Director import Director
from CarBuilder import CarBuilder
from ManualBuilder import ManualBuilder

if __name__ == "__main__":
    director = Director()

    # Build a sports car and its manual
    car_builder = CarBuilder()
    manual_builder = ManualBuilder()

    director.set_builder(car_builder)
    director.makeSportsCar()
    car = car_builder.getResult()
    print(car)

    director.set_builder(manual_builder)
    director.makeSportsCar()
    manual = manual_builder.getResult()
    print(manual)

    print("\n")

    # Build an SUV and its manual
    director.set_builder(car_builder)
    director.makeSUV()
    car = car_builder.getResult()
    print(car)

    director.set_builder(manual_builder)
    director.makeSUV()
    manual = manual_builder.getResult()
    print(manual)
