#!/usr/bin/env python3
import re
from .helpers import header_helper
from .helpers import link_helper
from .helpers.org_markdown import PLACEHOLDER, ORG_MARKDOWN
from .helpers.wiki_regex import REGEX


def convert(text):
    _text = text
    for markdown_type, regex in REGEX.items():
        matches = re.finditer(regex, text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            _text = apply_substitution(_text, match, markdown_type)
    return _text


def generate_replacement(text, replacement_type):
    return ORG_MARKDOWN[replacement_type].replace(PLACEHOLDER, text)


def apply_replacement(full_text, original_markup, replacement_markup):
    return full_text.replace(original_markup, replacement_markup)


def apply_substitution(text, match_data, replacement_type):
    match_text = match_data.group(0)
    match_inner_text = match_data.group(1)
    replacement = ""

    match replacement_type:
        case "heading":
            heading_end = match_data.group(2)
            replacement = header_helper.generate_header(match_text, heading_end)
        case "wiki_link":
            replacement = link_helper.generate_link_replacement(match_data)
        case "code_block":
            replacement = generate_replacement(match_inner_text, replacement_type)
        case _:
            replacement = generate_replacement(match_inner_text, replacement_type)

    return apply_replacement(text, match_text, replacement)
