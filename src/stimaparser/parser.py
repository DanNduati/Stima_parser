#!/usr/bin/env python
import re
from pathlib import Path

from pdfminer.high_level import extract_text

PDF_FILE_PATH = "/home/daniel/Desktop/learn/stima_parser/pdfs"


def extract_pdftext(pdf_path: Path) -> str:
    text = extract_text(str(pdf_path))
    text = text.replace("\n", ".")
    # Substitute more than 2 white spaces in the text
    text = re.sub(r"[\s]{2,}", " ", text)
    return text


def parse_regions(text: str):
    regex = r"(?P<REGION>[A-Z]{2,}\s?[A-Z]{2,})+\s+REGION"
    matches = re.finditer(regex, text, re.MULTILINE)

    for match_num, match in enumerate(matches, start=1):
        print(
            f"Region Match {match_num} at {match.start()}-{match.end()}: {match.group()}"
        )
        # Region -> group 1
        print(
            f"Actual Region found at {match.start(1)}-{match.end(1)}: {match.group('REGION')}"
        )


def main():
    pdf_files = Path(PDF_FILE_PATH).glob("**/*.pdf")
    for pdf_file in pdf_files:
        print(f"{'*'*len(str(pdf_file))}")
        print(pdf_file)
        print(f"{'*'*len(str(pdf_file))}\n")
        text = extract_text(str(pdf_file))
        # print(repr(text))
        parse_regions(text)


if __name__ == "__main__":
    main()
