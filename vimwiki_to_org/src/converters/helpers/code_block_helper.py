#!/usr/bin/env python3


def generate_code_block(match_data):
    full_text = match_data.group(0)

    # replace first curly brackes
    _text = full_text.replace("{{{", "#+begin_src ", 1)
    # replace last curly brackets
    final = _text[:-3] + "\n#+end_src"

    return final
