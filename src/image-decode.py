import glob
import os

import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    pdfs = glob.glob(pdf_path)
    text = ""
    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 500)

        for pageNum, imgBlob in enumerate(pages):
            text += pytesseract.image_to_string(imgBlob, lang="spa")
    return text


def extract_pdf_text(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf = PdfReader(f)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text


def extract_image_text():
    csv_file = open("image.csv", "w")
    csv_file.write("filename, text\n")
    base_dir = "\\temp\\imageSamples"
    for file in os.listdir(base_dir):
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(base_dir + "\\" + file)
            text_witouth_commas = text.replace(",", " ")
            csv_file.write(f"{file}, {text_witouth_commas}\n")
            print(text)
            print("\n")
    csv_file.close()


if __name__ == "__main__":
    extract_image_text()
