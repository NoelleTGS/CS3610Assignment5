from WordDocumentCreator import WordDocumentCreator
from PDFDocumentCreator import PDFDocumentCreator
from ExcelDocumentCreator import ExcelDocumentCreator
from BronzeApp import BronzeApp
from GoldApp import GoldApp


if __name__ == "__main__":
    # Bronze tier app - only Word documents allowed
    bronze_creator = WordDocumentCreator()
    bronze_app = BronzeApp(bronze_creator)

    bronze_app.create_document()
    # If we try using a PDF creator in Bronze tier, it won't work
    pdf_creator = PDFDocumentCreator()
    bronze_app_with_pdf = BronzeApp(pdf_creator)
    bronze_app_with_pdf.create_document()

    # Gold tier app - supports both Word and PDF
    gold_word_creator = WordDocumentCreator()
    gold_pdf_creator = PDFDocumentCreator()
    gold_excel_creator = ExcelDocumentCreator()

    gold_app_word = GoldApp(gold_word_creator)
    gold_app_pdf = GoldApp(gold_pdf_creator)
    gold_app_excel = GoldApp(gold_excel_creator)

    gold_app_excel.create_document()
    gold_app_word.create_document()
    gold_app_pdf.create_document()
