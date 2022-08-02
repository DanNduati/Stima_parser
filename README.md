<h1 align="center"><b>Stima Parser</b></h1>

[![Project Status: WIP – Initial development is in progress.](https://www.repostatus.org/badges/latest/wip.svg)]()

## <b>Description</b>
Stima parser extracts interruption data from scheduled power interruptions pdf documents with regex pattern-matching for the following fields:

1. Region
2. County
3. Area
4. Date
5. Time
6. Mtaa

## <b>Prerequisites</b>
- Python3

## <b>Parser Current State</b>
Checkout the parser's output for the multiple documents [here](https://github.com/DanNduati/Stima_parser/tree/main/parser_output)

:warning: Garbage in, garbage out

The parser is **Regex-based** so it *will* fail on certain edge cases, which are scantly documented in the [repository issues](https://github.com/DanNduati/Stima_parser/issues).

## Built With
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- [Regex](https://docs.python.org/3/library/re.html)
- [Stima-scraper](https://github.com/DanNduati/Stima_scraper)

## <b>License and Copyright</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)

Copyright 2022 Daniel Chege Nduati
