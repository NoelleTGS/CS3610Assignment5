from abc import ABC, abstractmethod, Document

class DocumentCreator(ABC):

    @staticmethod
    @abstractmethod
    def factory_method() -> Document:
        pass

    @staticmethod
    @abstractmethod
    def create_document() -> str:
        pass