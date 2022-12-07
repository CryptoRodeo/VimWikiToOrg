HEADING_REGEX = {
    "heading" : "^=*(.*[^=])(={1,6})$",
}

MULTILINE_REGEX = {
    "code_block" : "\{{3}((\n|.)*?)\}{3}",
}

LIST_REGEX = {
    "asterisk_list_item" : "^\*(.+([^\*])$)",
}

LINK_REGEX = {
    "wiki_link" : "\[\[(.*)\]\]",
    "link_with_description": "\[\[(.*)\|(.*)\]\]",
    "file_link" : "\{{2}(file:.*)\}{2}",
}

TEXT_FORMATTING_REGEX = {
    "bold_text" : "(\*(.*)\*$)",
    "inline_code" : "\`(.*)\`",
    "italic_text": "\s_(.*)_\s",
}

REGEX_BY_PRIORITY = [
    HEADING_REGEX,
    MULTILINE_REGEX,
    LINK_REGEX,
    LIST_REGEX,
    TEXT_FORMATTING_REGEX,
]
