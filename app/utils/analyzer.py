import pdfplumber


def extract_text_from_pdf(file) -> str:
    try:
        with pdfplumber.open(file.file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception as e:
        return ""
