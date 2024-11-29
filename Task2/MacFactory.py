from Task2 import Button, Checkbox
from Task2.IGUIFactory import IGUIFactory
from Task2.MacButton import MacButton
from Task2.MacCheckbox import MacCheckbox


class MacFactory(IGUIFactory):
    def createButton(self) -> Button:
        print("I am making a Mac button")
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        print("I am making a Mac checkbox")
        return MacCheckbox()
