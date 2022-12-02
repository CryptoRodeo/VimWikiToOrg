import re

# Regex References
###############################
#

heading = r"^=(.*)={1,}$"

# heading 1, 2, 3...
heading_2 = "^=(.*)={2}$"
heading_3 = "^=(.*)={3}$"
heading_4 = "^=(.*)={4}$"
heading_5 = "^=(.*)={5}$"

# Italic markup
italic = "_(.*)_"

# Inline code
inline_code = "`(.*)`"

# links
basic_link = "\[\[(.*)\]\]"
link_with_description = "\[\[((.*)\|{1}.*)\]\]"

# file links
file_link = "\{\{(file:.*)\}\}"

# Code block
code_block = "\{\{\{([^}]*)\}\}\}"

REGEX = {
    "heading"        : heading,
    "italic"         : italic,
    "inline_code"    : inline_code,
    "basic_link"     : basic_link,
    "file_link"      : file_link,
    "code_block"     : code_block,
}

REPLACEMENTS = {
    "heading"        : "* #" ,
    "italic"         : "/#/",
    "inline_code"    : "~#~",
    "basic_link"     : "[#]",
    "file_link"      : "[#]",
    "code_block"     : "begin_src\n#\nend_src",
}

REPLACEMENT_PLACEHOLDER = "#"


# generate headings based on level
def generate_header(header_txt, level):
    res = header_txt.replace("=",'')
    final = REPLACEMENTS["heading"].replace(REPLACEMENT_PLACEHOLDER, res)
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

    print(replacementType)
    return REPLACEMENTS[replacementType].replace(REPLACEMENT_PLACEHOLDER, text)

def getInnerText(rgx, mk_type, text):
    matches = re.finditer(rgx, text, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print ("Original => {match} ".format(match = match.group(0)))
        print(applyReplacement(match.group(1), mk_type))
#        if mk_type == "heading":
#            hding_level = find_header_level(match.group(0))
#            print(generate_header(match.group(1), hding_level))
#            return generate_header(match.group(1), hding_level)
#            applyReplacement(match.group(0), mk_type)
#        else:
#            applyReplacement(match.group(1), mk_type)
#        print(applyReplacement(match.group(1), mk_type))


# Headings
#==============================
test_text = '=Chapter one='
#print(getInnerText(heading, test_text))

# Text Styles
###############################
# Italic
test_text = "_and So it goes_"
#print(getInnerText(italic, test_text))

# Inline code
test_text= "`echo 'Hello'`"
#print(getInnerText(inline_code, test_text))

# Links
###############################
#
# Basic
test_text = "[[www.link_to_somewhere.com]]"
#print(getInnerText(basic_link, test_text))

## with description
test_text = "[[www.link_to_somewhere.com | a link to somewhere]]"
#print(getInnerText(link_with_description, test_text))

## file
test_text = "{{file:./some-file.png}}"
#print(getInnerText(file_link, test_text))

## Code block
test_text = """
{{{python
  print()
  def funk():
    doTheThing()
}}}
"""

#print(getInnerText(code_block, test_text))

## Read a file, save it's contents to a string var
file_text = ""
with open("./TestHeaders.wiki", 'r') as f:
    file_text = f.read()

getInnerText(heading,"heading",file_text)

#for markdown_type, regex in REGEX.items():
#    getInnerText(regex, markdown_type, file_text)
