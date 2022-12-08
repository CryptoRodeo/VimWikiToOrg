#!/usr/bin/env python3
from vimwiki_to_org.src.converters.vimwiki_to_org import previously_converted


def already_converted(txt):
    return previously_converted(txt)
