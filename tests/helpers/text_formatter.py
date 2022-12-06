from textwrap import dedent
from vimwiki_to_org.src.converters.helpers.prevention_tag import PREVENTION_TAG
from vimwiki_to_org.src.converters.vimwiki_to_org import convert

def format_text(txt):
    formatted = dedent(txt)
    return formatted

def format_text_after_conversion(txt):
    txt = format_text(txt)
    return remove_prevention_tag(txt)

def remove_prevention_tag(txt):
    return txt.replace(PREVENTION_TAG, '')

def assert_conversion_results(data={}):
    for wiki_markup, expected_output in data.items():
        actual = format_text_after_conversion(convert(wiki_markup))
        assert actual == expected_output
