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
Checkout the parser's output for the different documents and fields [here](https://github.com/DanNduati/Stima_parser/tree/main/parser_output)

> :warning: Garbage in, garbage out

Most of the current issues however are caused by inconsistent pdf formating which affects pattern-matching.

## ToDo
- [ ] Handle descrepancies in pdf formats()
- [ ] Test(s)
- [ ] Consolidate matches per pdf

## Built With
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- [Regex](https://docs.python.org/3/library/re.html)
- [Stima-scraper](https://github.com/DanNduati/Stima_scraper)

## <b>License and Copyright</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)

Copyright 2022 Daniel Chege Nduati