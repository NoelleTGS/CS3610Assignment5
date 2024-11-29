from abc import ABC, abstractmethod

'''Document interface'''

class Document(ABC):
    
    @staticmethod
    @abstractmethod
    def create()-> None: #A static interface method
        pass