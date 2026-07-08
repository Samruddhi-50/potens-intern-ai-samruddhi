import fitz  # PyMuPDF
import os

def load_documents(folder_path):
    documents = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file_name)

            pdf = fitz.open(pdf_path)

            for page_num in range(len(pdf)):
                page = pdf.load_page(page_num)

                documents.append({
                    "file": file_name,
                    "page": page_num + 1,
                    "text": page.get_text()
                })

            pdf.close()

    return documents
    