REGEX = {
    "heading"    : "^=*(.*[^=])(={1,6})$",
    "italic"     : "_(.*)_",
    "inline_code": "`(.*)`",
    "wiki_link"       : "\[\[(.*)\]\]",
    "link_with_description": "\[\[(.*)\|(.*)\]\]",
    "file_link"  : "\{{2}(file:.*)\}{2}",
    "code_block" : "\{{3}([^}]*)\}{3}",
}
