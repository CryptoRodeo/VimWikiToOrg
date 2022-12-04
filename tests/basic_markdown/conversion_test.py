#!/usr/bin/env python3

import pytest
from textwrap import dedent
from vimwiki_to_org.src.converters.vimwiki_to_org import convert

def test_basic_markup_conversions():

    wiki_code_block = dedent("""\
    {{{python
    print("Hello World")
    }}}""")

    org_code_block = dedent("""\
    #+begin_src python
    print("Hello World")

    #+end_src""")

    test_data = {
        "= header =":"* header ",
        "_italic text_":"/italic text/",
        "`print('hello')`":"~print('hello')~",
        "[[OtherWiki]]":"[[file:OtherWiki.org]]",
        wiki_code_block : org_code_block,
    }

    assert_conversion_result(test_data)

def test_converting_different_header_levels():
    test_data = {
        "= header ="          :"* header ",
        "== header =="        :"** header ",
        "=== header ==="      :"*** header ",
        "==== header ===="    :"**** header ",
        "===== header ====="  :"***** header ",
        "====== header ======":"****** header ",
    }

    assert_conversion_result(test_data)


def assert_conversion_result(data={}):
    for wiki_markup, expected_output in data.items():
        assert convert(wiki_markup) == expected_output
