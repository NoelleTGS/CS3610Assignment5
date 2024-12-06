from abc import ABC, abstractmethod

from Task2.IGUIFactory import IGUIFactory


class Application(ABC):
    def __init__(self, factory: IGUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    @abstractmethod
    def createUI(self):
        self.button = self.factory.createButton()
        self.checkbox = self.factory.createCheckbox()

    @abstractmethod
    def paint(self):
        self.button.paint()
