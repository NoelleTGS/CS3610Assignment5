from abc import ABC

'''Document'''

class Document(ABC):
    
    def __init__(self):
        self.__name = "Document"

    def create(self):
        return f"Creating {self.__name}"