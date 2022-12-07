#!/usr/bin/env python3
import re
from .helpers import header_helper
from .helpers import link_helper
from .helpers.org_markdown import PLACEHOLDER, ORG_MARKDOWN
from .helpers.wiki_regex import REGEX_BY_PRIORITY
from .helpers.prevention_tag import PREVENTION_TAG


def convert(text):
    _text = text
    for type_regex in REGEX_BY_PRIORITY:
        for markdown_type, regex in type_regex.items():
            matches = re.finditer(regex, _text, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                _text = apply_substitution(_text, match, markdown_type)

    return _text


def generate_replacement(text, replacement_type):
    return ORG_MARKDOWN[replacement_type].replace(PLACEHOLDER, text)


def apply_replacement(full_text, original_markup, replacement_markup):
    # tag with prevention tag to avoid accidental overrides
    new_markup = (replacement_markup + PREVENTION_TAG)

    return full_text.replace(original_markup, new_markup)


def apply_substitution(text, match_data, replacement_type):
    match_text = match_data.group(0)
    match_inner_text = match_data.group(1)
    replacement = ""

    # Prevent overrides
    if previously_converted(match_text):
        return text

    if asterisk_markdown_type(replacement_type):
        return handle_asterisk_case(text, match_data, replacement_type)

    if text_emphasis_type(replacement_type):
        return handle_text_emphasis(text, match_data, replacement_type)

    match replacement_type:
        case "heading":
            heading_end = match_data.group(2)
            replacement = header_helper.generate_header(match_text, heading_end)
        case "wiki_link":
            replacement = link_helper.generate_link_replacement(match_data)
        case _:
            replacement = generate_replacement(match_inner_text, replacement_type)

    return apply_replacement(text, match_text, replacement)


def previously_converted(text):
    return PREVENTION_TAG in text


def asterisk_markdown_type(match_type):
    return match_type in ["bold_text", "asterisk_list_item"]


def handle_asterisk_case(text, match_data, match_type):
    match_text = match_data.group(0)
    inner_text = match_data.group(1)
    replacement = ""

    if match_text.count("*") > 1:
        replacement = generate_replacement(match_text, "bold_text")
    else:
        replacement = generate_replacement(inner_text, match_type)

    return apply_replacement(text, match_text, replacement)


def handle_text_emphasis(text, match_data, match_type):
    match_text = match_data.group(0)
    replacement = ""

    match match_type:
        case "inline_code":
            # sometimes multiple lines are captured, so lets individually
            # swap out the ` characters instead of doing it by regex groups.
            replacement = match_text.replace("`", "~")
        case "italic_text":
            # same issue as the previous case
            replacement = match_text.replace("_", "/")

    return apply_replacement(text, match_text, replacement)


def text_emphasis_type(match_type):
    return match_type in ["italic_text", "inline_code"]
