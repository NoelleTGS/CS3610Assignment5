from Document import Document
from DocumentCreator import DocumentCreator
from ExcelDocument import ExcelDocument

class ExcelDocumentCreator(DocumentCreator):
    def factory_method(self) -> Document:
        return ExcelDocument()
