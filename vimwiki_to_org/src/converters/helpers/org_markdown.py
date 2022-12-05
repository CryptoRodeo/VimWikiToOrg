PLACEHOLDER = "<^>"
DESCRIPTION_PLACEHOLDER = "<->"
ORG_MARKDOWN = {
    "heading"              : f"{PLACEHOLDER}",
    "italic"               : f"/{PLACEHOLDER}/",
    "inline_code"          : f"~{PLACEHOLDER}~",
    "wiki_link"            : f"[[file:{PLACEHOLDER}]]",
    "file_link"            : f"[[{PLACEHOLDER}]]",
    "link_with_description": f"[[{PLACEHOLDER}][{DESCRIPTION_PLACEHOLDER}]]",
    "code_block"           : f"#+begin_src {PLACEHOLDER}\n#+end_src",
}
