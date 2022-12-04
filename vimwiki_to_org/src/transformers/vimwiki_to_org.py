#!/usr/bin/env python3
import re
from .helpers.header_helper import HeaderHelper


REGEX = {
    "heading"    : "^=*(.*[^=])(={1,6})$",
    "italic"     : "_(.*)_",
    "inline_code": "`(.*)`",
    "link"       : "\[\[(.*)\]\]",
    "file_link"  : "\{{2}(file:.*)\}{2}",
    "code_block" : "\{{3}([^}]*)\}{3}",
}

PLACEHOLDER = "<^>"

_REPLACEMENT_MARKDOWN = {
    "heading"    : "* {}" ,
    "italic"     : "/{}/",
    "inline_code": "~{}~",
    "link"       : "[[file:{}]]",
    "file_link"  : "[[{}]]",
    "code_block" : "#+begin_src {}\n#+end_src",
}

ORG_MARKDOWN = { markdown: replacement.format(PLACEHOLDER) for markdown, replacement in _REPLACEMENT_MARKDOWN.items() }

header_helper = HeaderHelper(ORG_MARKDOWN["heading"], PLACEHOLDER)


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


def generate_link_replacement(full_text, original_markup, link_text):
    _text = link_text + '.org'
    replacement = generate_replacement(_text, "link")
    return apply_replacement(full_text, original_markup, replacement)


def apply_substitution(text, regex, match, replacement_type):
    match_text = match.group(0)
    match_inner_text = match.group(1)

    if replacement_type == "heading":
        heading_end = match.group(2)
        replacement = header_helper.generate_header(match_inner_text, heading_end)
        return apply_replacement(text, match_text, replacement)

    if replacement_type == "link":
        return generate_link_replacement(text, match_text, match_inner_text)

    replacement = generate_replacement(match_inner_text, replacement_type)
    return apply_replacement(text, match_text, replacement)
