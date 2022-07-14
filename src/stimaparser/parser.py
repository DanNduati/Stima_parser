#!/usr/bin/env python
from pathlib import Path
import re
from pdfminer.high_level import extract_text

PDF_FILE_PATH = "/home/daniel/Desktop/learn/stima_parser/pdfs"


def extract_pdftext(pdf_path: Path) -> str:
    text = extract_text(str(pdf_path))
    text = text.replace("\n", ".")
    # Substitute more than 2 white spaces in the text
    text = re.sub(r"[\s]{2,}", " ", text)
    return text


def main():
    pdf_files = Path(PDF_FILE_PATH).glob("**/*.pdf")
    for pdf_file in pdf_files:
        print(f"{'*'*len(str(pdf_file))}")
        print(pdf_file)
        print(f"{'*'*len(str(pdf_file))}\n")
        text = extract_text(str(pdf_file))
        # print(repr(text))


if __name__ == "__main__":
    main()
