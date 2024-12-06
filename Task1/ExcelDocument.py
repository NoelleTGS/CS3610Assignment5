import Document

'''
Excel Class implements document interface
'''
class ExelDocument(Document):  
    def __init__(self):
        self.__name = "Excel Document"

    def create(self):
        return f"Creating {self.__name}"