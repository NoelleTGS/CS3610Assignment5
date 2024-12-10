from abc import ABC, abstractmethod
from Document import Document

class DocumentCreator(ABC):
    @abstractmethod
    def factory_method(self) -> Document:
        pass