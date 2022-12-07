from textwrap import dedent
from vimwiki_to_org.src.converters.vimwiki_to_org import convert
from .prevention_tag import prevention_tag

def format_text(txt):
    """
    Formats test text after conversion by removing indents
    """
    formatted = dedent(txt)
    return formatted

def format_text_after_conversion(txt):
    """
    Formats test text after conversion
    """

    # handle italics...
    if "italic" in txt:
        return remove_prevention_tag(txt)

    txt = format_text(txt)

    return remove_prevention_tag(txt)

def remove_prevention_tag(txt):
    """
    Removes the global prevention tag from converted text
    """
    return txt.replace(prevention_tag(), '')
