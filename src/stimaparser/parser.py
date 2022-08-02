#!/usr/bin/env python
import re
from itertools import chain
from pathlib import Path

from pdfminer.high_level import extract_text

from utils import (  # isort:skip
    REGION_REGEX,
    COUNTY_REGEX,
    AREA_REGEX,
    DATE_REGEX,
    TIME_REGEX,
    MTAA_REGEX,
)

PDF_FILE_PATH = "/home/daniel/Desktop/learn/stima_parser/pdfs"


class StimaParser:
    """
    A Parser class

    Attribute
    ---------
    document_path : str
        a path to a single interruption pdf document or directory of interruption pdf document(s)

    """

    def __init__(self, document_path: str):
        self.document_path = Path(document_path)

    def extract_pdftext(self, pdf_path: Path) -> str:
        """Extract text from a document"""
        with open(pdf_path, "rb") as f:
            text = extract_text(f)
        return text

    def parse_regions(self, text: str):
        region_matches = re.finditer(REGION_REGEX, text)
        return (
            [
                f"Region #{index}",
                match.group("REGION").strip(),
                match.start("REGION"),
                match.end("REGION"),
            ]
            for index, match in enumerate(region_matches)
        )

    def parse_counties(self, text: str):
        county_matches = re.finditer(COUNTY_REGEX, text)
        return (
            [
                f"County #{index}",
                match.group("COUNTY").strip(),
                match.start("COUNTY"),
                match.end("COUNTY"),
            ]
            for index, match in enumerate(county_matches)
        )

    def parse_areas(self, text: str):
        area_matches = re.finditer(AREA_REGEX, text)
        return (
            [
                f"Area #{index}",
                match.group("AREA").strip(),
                match.start("AREA"),
                match.end("AREA"),
            ]
            for index, match in enumerate(area_matches)
        )

    def parse_date(self, text: str):
        date_matches = re.finditer(DATE_REGEX, text)
        return (
            [
                f"Date #{index}",
                match.group("DATE").strip(),
                match.start("DATE"),
                match.end("DATE"),
            ]
            for index, match in enumerate(date_matches)
        )

    def parse_time(self, text: str):
        time_matches = re.finditer(TIME_REGEX, text)
        return (
            [
                f"Time #{index}",
                match.group("TIME").strip(),
                match.start("TIME"),
                match.end("TIME"),
            ]
            for index, match in enumerate(time_matches)
        )

    def parse_mtaa(self, text: str):
        mtaa_matches = re.finditer(MTAA_REGEX, repr(text))
        return (
            [
                f"Mtaa #{index}",
                match.group("MTAA").strip(),
                match.start("MTAA"),
                match.end("MTAA"),
            ]
            for index, match in enumerate(mtaa_matches)
        )

    def consolidate_matches(self, text: str, document: Path):
        # Go over all match object iterators, consolidate matches
        # for Region -> County -> Area ->[date,time,mtaa] and serialize output
        print(f"{'*'*len(str(document))}")
        print(document)
        print(f"{'*'*len(str(document))}\n")
        # make an iterator of all match objects
        matches = chain(
            self.parse_regions(text),
            self.parse_counties(text),
            self.parse_areas(text),
            self.parse_date(text),
            self.parse_time(text),
            self.parse_mtaa(text),
        )
        for match in matches:
            print(match)
        # todo: serialization logic

    def parse_data(self):
        if self.document_path.is_dir():
            documents = self.document_path.glob("**/*.pdf")
            for document in documents:
                text = self.extract_pdftext(document)
                # self.print_matches(text, document)
                self.consolidate_matches(text, document)
        if self.document_path.is_file():
            if self.document_path.suffix == ".pdf":
                document = self.document_path
                text = self.extract_pdftext(document)
                # self.print_matches(text, document)
                self.consolidate_matches(text, document)


def main():
    # Directory with multiple files
    parser = StimaParser(document_path=PDF_FILE_PATH)
    """
    # Single document
    parser = StimaParser(
        document_path="/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf"
    )
    """
    parser.parse_data()


if __name__ == "__main__":
    main()
