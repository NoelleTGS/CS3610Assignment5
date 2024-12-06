from Task3.CarBuilder import CarBuilder
from Task3.Director import Director

director = Director()
print(1)
builder = CarBuilder()
print(2)

director.builder = builder
print(3)