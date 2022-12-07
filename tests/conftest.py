import pytest
from .helpers.text_formatter import format_text
from .helpers.text_conversion import convert
from .helpers.markdown_classifier import classify_markdown


@pytest.fixture
def basic_markdown_data():
    # code blocks
    wiki_code_block = format_text("""\
    {{{python
    print("Hello World")
    }}}""")

    org_code_block = format_text("""\
    #+begin_src python
    print("Hello World")

    #+end_src""")

    # links
    wiki_link_w_description = "[[some wiki|description for some wiki file]]"
    org_link_w_description = "[[some wiki.org][description for some wiki file]]"
    wiki_file_link = "{{file:./some-image.png}}"
    org_file_link = "[[file:./some-image.png]]"
    # lists
    wiki_bullet_list = format_text("""\
    * bullet list item 1
    * bullet list item 2
    """)

    org_dash_list = wiki_bullet_list.replace('*', '-')

    return {
        "= header ="            :"* header ",
        "== header =="          :"** header ",
        "=== header ==="        :"*** header ",
        "==== header ===="      :"**** header ",
        "===== header ====="    :"***** header ",
        "====== header ======"  :"****** header ",
        "*bold*"                :"*bold*",
        " _italic_ "            :" /italic/ ",
        "`print('hello')`"      :"~print('hello')~",
        "[[OtherWiki]]"         :"[[file:OtherWiki.org]]",
        "`echo '42'`"           : "~echo '42'~",
        wiki_link_w_description : org_link_w_description,
        wiki_file_link          : org_file_link,
        wiki_code_block         : org_code_block,
        wiki_bullet_list        : org_dash_list,
    }

@pytest.fixture
def markdown_during_conversion(basic_markdown_data):
    res = basic_markdown_data
    for wiki_markdown, _ in res.items():
        res[wiki_markdown] = convert(wiki_markdown)

    return res

@pytest.fixture
def markdown_with_classifiers():
    code_block = format_text("""\
    {{{python
        print('Hello World')
     }}}
    """)

    wiki_bullet_list = format_text("""\
    * bullet list item 1
    """)

    data = {
        "= header ="                                    : "heading",
        "== header =="                                  : "heading",
        "=== header ==="                                : "heading",
        "==== header ===="                              : "heading",
        "===== header ====="                            : "heading",
        "====== header ======"                          : "heading",
        "`print('hello')`"                              : "inline_code",
        "*bold*"                                        : "bold_text",
        " _italic_ "                                    : "italic_text",
        "[[OtherWiki]]"                                 : "wiki_link",
        "`echo '42'`"                                   : "inline_code",
        "[[some wiki|description for some wiki file]]"  : "link_with_description",
        "{{file:./some-image.png}}"                     : "file_link",
        code_block                                      : "code_block",
        wiki_bullet_list                                : "asterisk_list_item"

     }

    return data
