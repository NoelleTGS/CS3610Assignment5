from abc import ABC, abstractmethod

class DocumentCreator(ABC):

    @staticmethod
    @abstractmethod
    def factory_method() -> Document:
        pass

    @staticmethod
    @abstractmethod
    def create_document() -> str:
        pass