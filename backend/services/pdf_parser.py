import fitz
from pathlib import Path


class PDFParser:

    @staticmethod
    def extract_text(pdf_path: str):

        pdf_file = Path(pdf_path)

        if not pdf_file.exists():
            raise FileNotFoundError(f"{pdf_path} not found")

        document = fitz.open(pdf_file)

        extracted_pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text")

            text = (
                text.replace("\n", " ")
                    .replace("\t", " ")
                    .strip()
            )

            extracted_pages.append({
                "page": page_number,
                "text": text
            })

        document.close()

        return extracted_pages