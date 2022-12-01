import re

# Regex References
###############################
#
# Use this to find the vimwiki headings
heading = r"^=(.*)=$"

# heading 1, 2, 3...
heading_1 = r"^=(.*)={1}$"
heading_2 = r"^=(.*)={2}$"
heading_3 = r"^=(.*)={3}$"

# Italic markup
italic = r"_(.*)_"

# Inline code
inline_code = r"`(.*)`"

# links
basic_link = r"\[\[(.*)\]\]"
link_with_description = r"\[\[((.*)\|{1}.*)\]\]"

# file links
file_link = r"\{\{(file:.*)\}\}"

# Code block
code_block = "\{\{\{([^}]*)\}\}\}"


def getInnerText(rgx, text):
    res = re.search(rgx, text)
    if res:
        f = res.group(1)
        return f
    return None

# Headings
#==============================
heading = "^=(.*)=$"
test_text = '=Chapter one='
print(getInnerText(heading, test_text))

# Text Styles
###############################
# Italic
test_text = "_and So it goes_"
print(getInnerText(italic, test_text))

# Inline code
test_text= "`echo 'Hello'`"
print(getInnerText(inline_code, test_text))

# Links
###############################
#
# Basic
test_text = "[[www.link_to_somewhere.com]]"
print(getInnerText(basic_link, test_text))

## with description
test_text = "[[www.link_to_somewhere.com | a link to somewhere]]"
print(getInnerText(link_with_description, test_text))

## file
test_text = "{{file:./some-file.png}}"
print(getInnerText(file_link, test_text))

## Code block
test_text = """
{{{python
  print()
  def funk():
    doTheThing()
}}}
"""
print(getInnerText(code_block, test_text))
