#!/usr/bin/env python3
import re


# generate headings based on level
def pad_header(header_txt, level):
    # remove any old headers if needed
    txt = header_txt.replace("=", '')

    final = txt.rjust(len(txt) + level , "*")
    return final


def find_header_level(txt):
    # Worst case, return a top level heading.
    level = 1

    for x in range(1, 8):
        level = x
        rgx = ("^(={%s})$" % level)

        # Keep going until we find a match
        if re.match(rgx, txt, re.MULTILINE):
            return level

    return level


def generate_header(inner_text, header_end):
    heading_level = find_header_level(header_end)
    header = pad_header(inner_text, heading_level)
    return header
