#!/usr/bin/env python3
import re
from vimwiki_to_org.src.converters.helpers.wiki_regex import REGEX

def classify_markdown(txt):
    """
    Returns the classification for a specific vim wiki markdown
    """
    for markdown_type, regex in REGEX.items():
        if re.findall(regex, txt):
            match markdown_type:
                case "wiki_link":
                    if ("|" in txt):
                        return "link_with_description"
                    else:
                        return markdown_type
                case _:
                    return markdown_type
