import fitz  # PyMuPDF

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text

# Function to truncate or summarize document text if it's too long
def truncate_text(text, max_length=6000):
    if len(text) > max_length:
        return text[:max_length] + "\n... [Truncated]"
    return text
