from Task2.Button import Button


class WinButton(Button):
    def __init__(self):
        print("Windows button initialized")

    @staticmethod
    def print():
        print("Windows button printing")