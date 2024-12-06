import os

from Task2.Application import Application
from Task2.MacFactory import MacFactory
from Task2.WinFactory import WinFactory

os_version = os.name

if os_version == "posix":
    factory = MacFactory()
else:
    factory = WinFactory()

app = Application(factory)

app.createUI()
app.paint()
