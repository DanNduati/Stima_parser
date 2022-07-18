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
    regex = r"(?P<REGION>[A-Z.]{2,}\s?[A-Z]{2,})+\s+REGION"
    matches = re.finditer(regex, text, re.MULTILINE)

    for match_num, match in enumerate(matches, start=1):
        print(
            f"Region Match {match_num} at {match.start()}-{match.end()}: {match.group()}"
        )
        # Region -> group 1
        print(
            f"Actual Region found at {match.start(1)}-{match.end(1)}: {match.group('REGION')}"
        )


def parse_counties(text):
    regex = r"(\bOF\s)?(?P<COUNTY>[A-Z]+\s?[A-Z]+\s)COUNTY"
    matches = re.finditer(regex, text, re.MULTILINE)
    for match_num, match in enumerate(matches, start=1):
        print(
            f"County Match {match_num} at {match.start()}-{match.end()}: {match.group()}"
        )
        # County -> group2
        print(
            f"Actual County found at {match.start(2)}-{match.end(2)}: {match.group('COUNTY')}"
        )


def parse_areas(text: str):
    regex = r"AREA:\s(?P<AREA>(([\w]){1,}[&,’'\(\)\s\w]+){1,})"
    matches = re.finditer(regex, text, re.MULTILINE)

    for match_num, match in enumerate(matches, start=1):
        print(
            f"Area Match {match_num} at {match.start()}-{match.end()}: {match.group().strip()}"
        )
        # Area -> group 1
        print(
            f"Actual Area found at {match.start(1)}-{match.end(1)}: {match.group('AREA').strip()}"
        )


def parse_date(text: str):
    regex = r"DATE:\s?(?P<DATE>[a-zA-z]+\s?([0-9]{2}\.){2}[0-9]{4})"
    matches = re.finditer(regex, text, re.MULTILINE)
    for match_num, match in enumerate(matches, start=1):
        print(
            f"Date Match {match_num} at {match.start()}-{match.end()}: {match.group().strip()}"
        )
        # Date -> group 1
        print(
            f"Actual Date found at {match.start(1)}-{match.end(1)}: {match.group('DATE').strip()}"
        )


def parse_time(text: str):
    # I know i can simplify this regex but my head is currently fried
    regex = r"TIME:\s?(?P<TIME>((\d+)[\.\s]?)+\s?(\w\.){,2}\s[–-]\s+((\d+)[\.\s]){1,}\s?(\w\.){,2})"
    matches = re.finditer(regex, text, re.MULTILINE)
    for match_num, match in enumerate(matches, start=1):
        print(
            f"Time Match {match_num} at {match.start()}-{match.end()}: {match.group().strip()}"
        )
        # Time -> group 1
        print(
            f"Actual Time found at {match.start(1)}-{match.end(1)}: {match.group('TIME').strip()}"
        )


def parse_mtaa(text: str):
    # regex = r"(?<=P.M.\s)(?P<MTAA>.*?)(?=([A-Z]{4})|(Interruption))"
    regex = r"(?<=P.M.\s)(?P<MTAA>.*?)(?=(adjacent)|(Interruption))"
    matches = re.finditer(regex, repr(text), re.MULTILINE)

    for match_num, match in enumerate(matches, start=1):

        print(
            f"Mtaa Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}"
        )
        # Mtaa -> group 1
        print(
            f"Actual Mtaa found at {match.start(1)}-{match.end(1)}: {match.group('MTAA').strip()}"
        )


def main():
    pdf_files = Path(PDF_FILE_PATH).glob("**/*.pdf")
    for pdf_file in pdf_files:
        print(f"{'*'*len(str(pdf_file))}")
        print(pdf_file)
        print(f"{'*'*len(str(pdf_file))}\n")
        text = extract_text(str(pdf_file))
        # print(repr(text))
        # parse_regions(text)
        # parse_counties(text)
        # parse_areas(text)
        # parse_date(text)
        # parse_time(text)
        parse_mtaa(text)


if __name__ == "__main__":
    main()
