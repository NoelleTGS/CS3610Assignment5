from AppVersion import AppVersion

# Gold tier: Allows both Word and PDF document creation
class GoldApp(AppVersion):
    def create_document(self):
        document = self.creator.factory_method()
        document.create()