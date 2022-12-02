import re

REGEX = {
    "heading"              : "^=(.*)={1,}$",
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
    "basic_link"           : "[#]",
    "link_with_description": "[#]", # TODO
    "file_link"            : "[#]",
    "code_block"           : "begin_src #\rend_src",
}

REPLACEMENT_PLACEHOLDER = "#"

# generate headings based on level
def generate_header(header_txt, level):
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
    level = 1
    for x in range(1,7):
        # Adjust regex to check for different header levels
        rgx = ("^=(.*)={%s}$" % x)
        level = x
        # Keep going until we no longer have a match, return the last match.
        if not re.match(rgx, txt):
            return level

    # Worst case, return a top level heading.
    return level

def remove_whitespace(txt):
    return txt.replace(' ', '')

def generate_header_replacement(text):
    heading_level = find_header_level(text)
    return generate_header(text, heading_level)

def applyReplacement(text, replacementType):
    if replacementType == "heading":
        return generate_header_replacement(text)

    return REPLACEMENTS[replacementType].replace(REPLACEMENT_PLACEHOLDER, text)

def perform(rgx, mk_type, text):
    matches = re.finditer(rgx, text, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print ("Original => {match} ".format(match = match.group(0)))
        print(applyReplacement(match.group(1), mk_type))

## Read a file, save it's contents to a string var
file_text = ""
with open("./BasicMarkup.wiki", 'r') as f:
    file_text = f.read()

for markdown_type, regex in REGEX.items():
    perform(regex, markdown_type, file_text)
