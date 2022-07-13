#!/usr/bin/env python
from pathlib import Path

from pdfminer.high_level import extract_text

PDF_FILE_PATH = Path(__file__).parent.parent.absolute().joinpath("pdfs")


def extract_pdftext(pdf_path: Path) -> None:
    text = extract_text(str(pdf_path))
    print(repr(text))


def main():
    pdf_files = Path(PDF_FILE_PATH).glob("**/*.pdf")
    for pdf_file in pdf_files:
        print(f"{'*'*len(str(pdf_file))}")
        print(pdf_file)
        print(f"{'*'*len(str(pdf_file))}")
        text = extract_text(str(pdf_file))
        print(repr(text))


if __name__ == "__main__":
    main()
