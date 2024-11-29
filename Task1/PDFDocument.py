import Document

'''
PDF class implements Document interface
'''

class PDFDocument(Document):  
    def __init__(self):
        self.__name = "PDF Document"

    def create(self):
        return f"Creating {self.__name}"