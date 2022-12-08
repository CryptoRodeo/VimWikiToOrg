#!/usr/bin/env python3
import re
from vimwiki_to_org.src.converters.helpers.wiki_regex import REGEX_BY_PRIORITY

def classify_markdown(txt):
    """
    Returns the classification for a specific vim wiki markdown
    """
    for type_regex in REGEX_BY_PRIORITY:
        for markdown_type, regex in type_regex.items():
            if re.findall(regex, txt):
                match markdown_type:
                    case "wiki_link":
                        if ("|" in txt):
                            return "link_with_description"
                        else:
                            return markdown_type
                    case _:
                        return markdown_type
