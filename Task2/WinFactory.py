from Task2 import Button, Checkbox
from Task2.IGUIFactory import IGUIFactory
from Task2.WinButton import WinButton
from Task2.WinCheckbox import WinCheckbox


class WinFactory(IGUIFactory):
    def createButton(self) -> Button:
        print("I am making a Windows button")
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        print("I am making a Windows checkbox")
        return WinCheckbox()
