from abc import ABC, abstractmethod

from Task2 import Button, Checkbox


# Abstract Interface for GUI Factory
class IGUIFactory(ABC):

    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass
