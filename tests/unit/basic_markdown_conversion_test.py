#!/usr/bin/env python3

import pytest
from ..helpers.text_formatter import format_text, assert_conversion_results

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
        "`print('hello')`"      :"~print('hello')~",
        "[[OtherWiki]]"         :"[[file:OtherWiki.org]]",
        "`echo '42'`"           : "~echo '42'~",
        wiki_link_w_description : org_link_w_description,
        wiki_file_link          : org_file_link,
        wiki_code_block         : org_code_block,
        wiki_bullet_list        : org_dash_list,
    }

def test_basic_markup_conversions(basic_markdown_data):
    assert_conversion_results(basic_markdown_data)
