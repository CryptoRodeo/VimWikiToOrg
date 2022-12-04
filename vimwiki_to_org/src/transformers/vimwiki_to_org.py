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
            _text = apply_substitution(_text, regex, match, markdown_type)
    return _text


def generate_replacement(text, replacement_type):
    return ORG_MARKDOWN[replacement_type].replace(PLACEHOLDER, text)


def apply_replacement(full_text, original_markup, replacement_markup):
    return full_text.replace(original_markup, replacement_markup)


def apply_substitution(text, regex, match, replacement_type):
    match_text = match.group(0)
    match_inner_text = match.group(1)

    if replacement_type == "heading":
        heading_end = match.group(2)
        replacement = header_helper.generate_header(match_text, heading_end)
        return apply_replacement(text, match_text, replacement)

    if replacement_type == "wiki_link":
        replacement = link_helper.generate_link_replacement(match)
        return apply_replacement(text, match_text, replacement)

    replacement = generate_replacement(match_inner_text, replacement_type)
    return apply_replacement(text, match_text, replacement)
