from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path):
    # Ouvrir le fichier PDF
    reader = PdfReader(file_path)
    text = ""

    # Extraire le texte de chaque page
    for page in reader.pages:
        text += page.extract_text()

    return text