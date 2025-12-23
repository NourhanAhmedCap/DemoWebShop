from playwright.sync_api import Page
from pypdf import PdfReader
import io
class basicsMethods():
   
    def __init__(self, page: Page):
        self.page = page

    def ClickonButton(self, Locator):
        self.page.locator(Locator).click()

    def logout_after_test(self):
        self.page.locator(".ico-logout").click()
    
    def ClickonElementwithFilter(self, Locator,text ):
        self.page.locator(Locator).filter(has_text=text).click()

    def download_file(self, OrderNumber):
            with self.page.expect_download() as d:
                self.page.locator(".pdf-order-button").click()
                d.value.save_as(f"C:/Users/nourahme/Downloads/Order_{OrderNumber}.pdf")
    

    def verify_texts_in_pdf(self, path, expected_texts):
        reader = PdfReader(path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() or ""

        for value in expected_texts:
            assert value in full_text, f"'{value}' not found in PDF"

    def pdf_content(self, path):
            reader = PdfReader(path)
            for i, page in enumerate(reader.pages, start=1):
                 text = page.extract_text()
                 print(f"\n--- Page {i}-----\n")
                 print(text)

