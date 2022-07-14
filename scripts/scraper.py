from pathlib import Path

from stimascraper.scraper import StimaScraper

PDF_FILE_PATH = "/home/daniel/Desktop/learn/stima_parser/pdfs/"


def main():
    scraper = StimaScraper(pdf_path=PDF_FILE_PATH)
    scraper.scrape()


if __name__ == "__main__":
    main()
