import re

# Regex References
###############################
#

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
    matches = re.finditer(rgx, text, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):

        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

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

## Read a file, save it's contents to a string var
file_text = ""
with open("./FIRE.wiki", 'r') as f:
    file_text = f.read()

#print(getInnerText("^=(.*)=$", file_text))

# Scann through text for headings found.
regex = "^=(.*)=$"
getInnerText(regex, file_text)
