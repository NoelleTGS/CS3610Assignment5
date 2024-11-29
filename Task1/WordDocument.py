import Document

'''
Word class implements Document interface
'''

class WordDocument(Document):  
    def __init__(self):
        self.__name = "Word Document"

    def create(self):
        return f"Creating {self.__name}"