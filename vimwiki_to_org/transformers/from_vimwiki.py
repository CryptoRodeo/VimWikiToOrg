#!/usr/bin/env python3
import re, glob, os

REGEX = {
#    "heading"              : "^=(.*)={1,}$", # original
    "heading"              : "^=*(.*[^=])(={1,6})$",
    "italic"               : "_(.*)_",
    "inline_code"          : "`(.*)`",
    "link"                 : "\[\[(.*)\]\]",
    "file_link"            : "\{{2}(file:.*)\}{2}",
#    "link_with_description": "\[\[((.*)\|{1}.*)\]\]",
#    "file_link"            : "\{\{(file:.*)\}\}",
#    "code_block"           : "\{\{\{([^}]*)\}\}\}",
    "code_block"           :"\{{3}([^}]*)\}{3}"
}

PLACEHOLDER = "<^>"

_REPLACEMENT_HASH = {
    "heading"              : "* {}" ,
    "italic"               : "/{}/",
    "inline_code"          : "~{}~",
    "link"                 : "[[file:{}]]",
    "file_link"            : "[[{}]]",
#    "link_with_description": "[{}]",
#    "file_link"            : "[file:./{}]",
    "code_block"           : "#+begin_src {}\n#+end_src",
}

REPLACEMENTS = { markdown: replacement.format(PLACEHOLDER) for markdown, replacement in _REPLACEMENT_HASH.items() }

NEW_FILE_STORAGE = './ConvertedWikis/{}'.format('<^>')

def to_org( text):
    _text = text
    for markdown_type, regex in REGEX.items():
        matches = re.finditer(regex, text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            _text = apply_substitution(_text, regex, match, markdown_type)
    return _text

# generate headings based on level
def pad_header(header_txt, level):
    # If the level was > 1, theres a change there are still some vimwiki headers left
    txt = header_txt.replace("=",'')
    final = REPLACEMENTS["heading"].replace(PLACEHOLDER, txt)

    # If the level is one, no need for more * being added to the right.
    # The line above is the result we want.
    if level == 1:
        return final

    # Because the replacement template has a * already in it, we have to remove 1 level
    adjusted_level = (level - 1)
    return final.rjust(len(final) + adjusted_level ,"*")

def find_header_level(txt):
    # Worst case, return a top level heading.
    level = 1
    for x in range(1,8):
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

def generate_replacement(text, replacement_type):
    return REPLACEMENTS[replacement_type].replace(PLACEHOLDER, text)

def apply_replacement(full_text, original_markup, replacement_markup):
    return full_text.replace(original_markup, replacement_markup)

def generate_link_replacement(full_text, original_markup, link_text):
    final_text = link_text + '.org'
    replacement = generate_replacement(final_text, "link")
    return apply_replacement(full_text, original_markup, replacement)

def apply_substitution(text, regex, match, replacement_type):
    original_text = match.group(0)
    inner_text = match.group(1)

    if replacement_type == "heading":
        heading_end = match.group(2)
        replacement = generate_header(inner_text, heading_end)
        return apply_replacement(text, original_text, replacement)

    if replacement_type == "link":
        return generate_link_replacement(text, original_text, inner_text)

    replacement = generate_replacement(inner_text, replacement_type)
    return apply_replacement(text, original_text, replacement)
