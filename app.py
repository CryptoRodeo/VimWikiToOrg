import re

REGEX = {
#    "heading"              : "^=(.*)={1,}$", # original
    "heading"              : "^=*(.*[^=])(={1,6})$",
    "italic"               : "_(.*)_",
    "inline_code"          : "`(.*)`",
    "basic_link"           : "\[\[(.*)\]\]",
    "link_with_description": "\[\[((.*)\|{1}.*)\]\]",
    "file_link"            : "\{\{(file:.*)\}\}",
    "code_block"           : "\{\{\{([^}]*)\}\}\}",
}

REPLACEMENTS = {
    "heading"              : "* #" ,
    "italic"               : "/#/",
    "inline_code"          : "~#~",
    # TODO - links might need some work?
    "basic_link"           : "[#]",
    "link_with_description": "[#]",
    "file_link"            : "[#]",
    # TODO - verify
    "code_block"           : "begin_src #\rend_src",
}

REPLACEMENT_PLACEHOLDER = "#"

# generate headings based on level
def pad_header(header_txt, level):
    # If the level was > 1, theres a change there are still some vimwiki headers left
    txt = header_txt.replace("=",'')
    final = REPLACEMENTS["heading"].replace(REPLACEMENT_PLACEHOLDER, txt)

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

def get_header_level_regex(level):
    return ("^=*(.*[^=])(={%s})$" % level)

def remove_whitespace(txt):
    return txt.replace(' ', '')

def generate_header(inner_text, header_end):
    heading_level = find_header_level(header_end)
    rgx_for_level = get_header_level_regex(heading_level)
    return pad_header(inner_text, heading_level)

def generate_replacement(text, replacement_type):
    return REPLACEMENTS[replacement_type].replace(REPLACEMENT_PLACEHOLDER, text)

def apply_replacement(full_text, original_markup, replacement_markup):
    return full_text.replace(original_markup, replacement_markup)

def apply_substitution(text, regex, match, replacement_type):
    original_text = match.group(0)
    inner_text = match.group(1)
    if replacement_type == "heading":
        heading_end = match.group(2)
        replacement = generate_header(inner_text, heading_end)
        return apply_replacement(text, original_text, replacement)

    replacement = generate_replacement(inner_text, replacement_type)
    return apply_replacement(text, original_text, replacement)

def perform(text):
    final_text = text
    for markdown_type, regex in REGEX.items():
        matches = re.finditer(regex, text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            final_text = apply_substitution(final_text, regex, match, markdown_type)
    return final_text

## Read a file, save it's contents to a string var
file_text = ""
with open("./BasicMarkup.wiki", 'r') as f:
    file_text = f.read()

final_text = file_text

print(perform(file_text))

# NOTE:
# - I think italic conversion is broken.
