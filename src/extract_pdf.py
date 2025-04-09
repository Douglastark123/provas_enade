from typing import Union
from pathlib import Path
import pdfplumber

def extract_pdf_text(pdf: Union[str, Path]) -> str:
    """
    Extracts all text from a PDF file.

    Args:
        pdf (str or Path): Path to the PDF file.

    Returns:
        str: All extracted text from the PDF, separated by newlines.
    """
    extracted_text = ""

    try:
        with pdfplumber.open(pdf) as pdf_file:
            for page in pdf_file.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
    except Exception as e:
        print(f"[Error] Failed to extract text from PDF: {e}")
        return ""

    return extracted_text
