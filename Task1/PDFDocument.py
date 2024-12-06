import Document

'''
PDF Class implements document
'''
class PDFDocument():
    
    def __init__(self):
        self.__name = "PDF Document"

    def create(self):
        return f"Creating {self.__name}"