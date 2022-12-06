from .text_formatter import format_text_after_conversion
from .text_conversion import convert

def assert_conversion_results(data={}):
    """
    Asserts the result of a conversion

    Params:
    data: Dict, Key is the wiki markup, Value is the conversion result
    """
    for wiki_markup, expected_output in data.items():
        actual = format_text_after_conversion(convert(wiki_markup))
        assert actual == expected_output
