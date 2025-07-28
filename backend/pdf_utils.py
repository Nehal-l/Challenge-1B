import fitz  # PyMuPDF

def extract_text_by_page(pdf_path, max_pages=10):
    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        if i >= max_pages:
            break
        text = page.get_text().strip()
        if len(text) > 30:  # skip near-blank pages
            pages.append(text)

    return pages
