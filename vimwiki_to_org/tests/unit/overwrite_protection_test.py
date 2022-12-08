#!/usr/bin/env python3

import pytest
from ..helpers.conversion_checker import assert_conversion_results
from ..helpers.text_checks import already_converted

def test_can_determine_if_markup_already_converted(markdown_during_conversion):
    for _, pending_org_markdown in markdown_during_conversion.items():
        assert already_converted(pending_org_markdown)
