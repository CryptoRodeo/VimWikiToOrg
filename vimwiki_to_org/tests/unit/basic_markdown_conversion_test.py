#!/usr/bin/env python3

import pytest
from ..helpers.text_formatter import format_text
from ..helpers.conversion_checker import assert_conversion_results

def test_basic_markup_conversions(basic_markdown_data):
    """
    Tests that basic vimwiki markdown gets converted to
    its .org equivalent.
    """
    assert_conversion_results(basic_markdown_data)
