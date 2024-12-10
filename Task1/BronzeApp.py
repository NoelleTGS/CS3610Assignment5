from AppVersion import AppVersion
from WordDocument import WordDocument

# Bronze tier: Only allows Word document creation
class BronzeApp(AppVersion):
    def create_document(self):
        document = self.creator.factory_method()
        if isinstance(document, WordDocument):
            document.create()
        else:
            print("Bronze tier supports Word documents only.")