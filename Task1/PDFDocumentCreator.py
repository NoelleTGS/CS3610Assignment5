from Document import Document
from DocumentCreator import DocumentCreator
from PDFDocument import PDFDocument

class PDFDocumentCreator(DocumentCreator):
    def factory_method(self) -> Document:
        return PDFDocument()