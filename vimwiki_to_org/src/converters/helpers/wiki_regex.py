REGEX = {
    "heading"              : "^=*(.*[^=])(={1,6})$",
    "bold_text"            : "\*(.*)\*",
    "inline_code"          : "\`(.*)\`",
    "wiki_link"            : "\[\[(.*)\]\]",
    "link_with_description": "\[\[(.*)\|(.*)\]\]",
    "file_link"            : "\{{2}(file:.*)\}{2}",
    "code_block"           : "\{{3}((\n|.)*?)\}{3}",
    "asterisk_list_item"   : "^\*(.+([^\*])$)",
}
