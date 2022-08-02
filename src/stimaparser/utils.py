#!/usr/bin/env python
"""Utility functions for stimaparser"""
import re
from pathlib import Path

REGION_REGEX = re.compile(
    r"(?P<REGION>[A-Z.]{2,}\s?[A-Z]{2,})+\s+REGION", flags=re.MULTILINE
)
COUNTY_REGEX = re.compile(
    r"(\bOF\s)?(?P<COUNTY>[A-Z]+\s?[A-Z]+\s)COUNTY", flags=re.MULTILINE
)
# regex = r"AREA[:;]\s?(?P<AREA>(\w+[-&,–’\(\)\s]?\s){1,})"
AREA_REGEX = re.compile(
    r"AREA[:;]\s*(?P<AREA>(([\w]){1,}[-&,–’\(\)\s]+){1,})", flags=re.MULTILINE
)
DATE_REGEX = re.compile(
    r"DATE:?\s?(?P<DATE>[a-zA-z]+\s?([0-9]{2}\.){2}[0-9]{4})", flags=re.MULTILINE
)
# regex = r"TIME:\s?(?P<TIME>((\d+)[\.\s]?)+\s?(\w\.){,2}\s[–-]\s+((\d+)[\.\s]){1,}\s?(\w\.){,2})"
TIME_REGEX = re.compile(
    r"TIME:\s?(?P<TIME>\d+\.\d+\s+[AP]\.M.\s+[–-]\s+\d+\.\d+\s+[AP]\.M.)",
    flags=re.MULTILINE,
)
# regex = r"(?<=P.M.\s)(?P<MTAA>.*?)(?=([A-Z]{4})|(Interruption))"
MTAA_REGEX = re.compile(
    r"(?<=P.M.\s)(?P<MTAA>.*?)(?=(adjacent)|(Interruption))", flags=re.MULTILINE
)
