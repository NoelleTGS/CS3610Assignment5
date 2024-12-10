from abc import ABC, abstractmethod
from DocumentCreator import DocumentCreator

class AppVersion(ABC):
    def __init__(self, creator: DocumentCreator):
        self.creator = creator

    @abstractmethod
    def create_document(self):
        pass