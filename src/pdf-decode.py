import os
import re

import click
from PyPDF2 import PdfReader


def extract_pdf_text(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf = PdfReader(f)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text


def extract_text(text, regex):
    return re.findall(regex, text)


@click.command()
@click.option("--pdf_path", required=True, help="Path to the PDF file")
@click.option("--regex", required=True, help="Regex to extract the text")
@click.option("--output_path", help="Path to the output file")
@click.option("--verbose", is_flag=True, help="Print the output")
@click.option("--remove_text", help="Text to remove from the extracted text")
@click.option("--prefix", help="Prefix to add to the extracted text")
def pdf_decode(pdf_path, regex, output_path, verbose, remove_text, prefix):
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found")
        return
    if verbose:
        print(f"Extracting text from {pdf_path}")
    text = extract_pdf_text(pdf_path)
    if verbose:
        print(f"Extracting text using regex {regex}")
    matched = extract_text(text, regex)
    if remove_text:
        if verbose:
            print(f"Removing text {remove_text}")
        matched = [line.replace(remove_text, "").strip() for line in matched]

    if verbose:
        print(f"Writing output to {output_path}")

    output = "\n".join(f"{prefix}{line}" for line in matched)
    print(output)
    if output_path:
        with open(output_path, "w") as f:
            f.write(output)

    if verbose:
        print("Done!")


if __name__ == "__main__":
    pdf_decode()
