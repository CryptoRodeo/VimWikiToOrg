#!/usr/bin/env python3
import re


class HeaderHelper:

    def __init__(self, markdown, placeholder):
        self.markdown = markdown
        self.placeholder = placeholder

    # generate headings based on level
    def pad_header(self, header_txt, level):
        # remove any old headers if needed
        txt = header_txt.replace("=", '')
        final = self.markdown.replace(self.placeholder, txt)

        # If the level is one, no need for more * being added to the right.
        # The line above is the result we want.
        if level == 1:
            return final

        # Because the replacement template has a * already in it, we have to remove 1 level
        adjusted_level = (level - 1)
        return final.rjust(len(final) + adjusted_level , "*")

    def find_header_level(self, txt):
        # Worst case, return a top level heading.
        level = 1

        for x in range(1, 8):
            level = x
            rgx = ("^(={%s})$" % level)

            # Keep going until we find a match
            if re.match(rgx, txt, re.MULTILINE):
                return level

            return level

    def generate_header(self, inner_text, header_end):
        heading_level = self.find_header_level(header_end)
        header = self.pad_header(inner_text, heading_level)
        return header
