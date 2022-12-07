import re
from .org_markdown import PLACEHOLDER, DESCRIPTION_PLACEHOLDER, ORG_MARKDOWN
from .wiki_regex import LINK_REGEX


def generate_replacement(data, replacement_type):
    if replacement_type == "link_with_description":
        res = ORG_MARKDOWN[replacement_type].replace(PLACEHOLDER, data["text"])
        return res.replace(DESCRIPTION_PLACEHOLDER, data["desc"])
    else:
        return ORG_MARKDOWN[replacement_type].replace(PLACEHOLDER, data["text"])


def build_basic_link(link_text):
    _text = link_text + '.org'
    replacement = generate_replacement({"text": _text}, "wiki_link")
    return replacement


def build_link_with_description(match_data):
    link_text = match_data.group(1)
    description = match_data.group(2)
    _text = link_text + '.org'

    data = {
        "text": _text,
        "desc": description
    }

    return generate_replacement(data, "link_with_description")


def generate_link_replacement(match_data):
    full_link_text = match_data.group(0)
    inner_link_text = match_data.group(1)

    actual_type = get_actual_link_type(full_link_text)

    if actual_type == "link_with_description":
        new_match_data = match_data_for_type("link_with_description", full_link_text)
        return build_link_with_description(new_match_data)
    else:
        return build_basic_link(inner_link_text)


def match_data_for_type(mkdown_type, text):
    if mkdown_type == "link_with_description":
        return re.match(LINK_REGEX["link_with_description"], text, re.MULTILINE)


def get_actual_link_type(full_link_text):
    if "|" in full_link_text:
        return "link_with_description"

    # assume it's a regular wiki link
    return "wiki_link"
