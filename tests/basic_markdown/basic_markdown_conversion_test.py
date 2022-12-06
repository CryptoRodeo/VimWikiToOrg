#!/usr/bin/env python3

import pytest
from textwrap import dedent
from vimwiki_to_org.src.converters.vimwiki_to_org import convert
from vimwiki_to_org.src.converters.helpers.prevention_tag import PREVENTION_TAG

def test_basic_markup_conversions():
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

    test_data = {
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

    assert_conversion_result(test_data)

def assert_conversion_result(data={}):
    for wiki_markup, expected_output in data.items():
        actual = format_text(convert(wiki_markup))
        assert actual == expected_output


def format_text(txt):
    formatted = dedent(txt)
    formatted = remove_prevention_tag(formatted)
    return formatted

def remove_prevention_tag(txt):
    return txt.replace(PREVENTION_TAG, '')
