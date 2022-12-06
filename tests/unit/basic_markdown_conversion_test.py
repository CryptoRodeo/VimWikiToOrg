#!/usr/bin/env python3

import pytest
from ..helpers.text_formatter import format_text, assert_conversion_results
from ..fixtures.basic_markdown_data import basic_markdown_data

def test_basic_markup_conversions(basic_markdown_data):
    assert_conversion_results(basic_markdown_data)
