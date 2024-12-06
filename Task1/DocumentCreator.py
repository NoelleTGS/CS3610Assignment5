from abc import ABC
from Document import Document
from ExcelDocument import ExcelDocument
from PDFDocument import PDFDocument
from WordDocument import WordDocument

#DocTypes = {'excel': ExcelDocument, 'pdf': PDFDocument, 'word': WordDocument}

class DocumentCreator:

    def factory_method(self) -> Document:
        pass

    @staticmethod
    def create_document(objType: str) -> Document: #A static method to get a concrete product

        if objType.lower() == 'excel':
            return ExcelDocument()
        if objType.lower() == 'pdf':
             return PDFDocument()
        if objType.lower() == 'word':
             return WordDocument()
        else:
            return Document()