# VimWiki To Org Mode 🦄
> Migration to Org mode, made a bit easier

![workflow](https://github.com/CryptoRodeo/VimWikiToOrg/actions/workflows/main.yml/badge.svg)

## What it does:

**Converts this:**

```
= Header1 =
== Header2 ==
=== Header3 ===
==== Heading4 ====
===== Heading5 =====
====== Heading6 ======

*bold text*
_italic text_

[[wiki_link]]
[[some wiki|description for some wiki file]]

* bullet list item 1
* bullet list item 2
    1) numbered list item 1
    2) numbered list item 2

{{{python
def greet(s):
    print("Hello, " + s)
}}}

`echo "42"`

| a table |  |
|---------|--|
|         |  |

{{file:./some-image.png}}

```

**To this:**


```
* Header1 
** Header2 
*** Header3 
**** Heading4 
***** Heading5 
****** Heading6 

*bold text*
/italic text/

[[file:wiki_link.org]]
[[some wiki.org][description for some wiki file]]

- bullet list item 1
- bullet list item 2
    1) numbered list item 1
    2) numbered list item 2

#+begin_src python
def greet(s):
    print("Hello, " + s)

#+end_src

~echo "42"~

| a table |  |
|---------|--|
|         |  |

[[file:./some-image.png]]

```

## Basic usage:

```
python vimwiki_to_org -h
usage: vimwiki_to_org [-h] [-d WIKI_PATH] [-o OUTPUT_PATH]

options:
  -h, --help            show this help message and exit
  -d WIKI_PATH, --wiki-path WIKI_PATH
                        absolute path to vimwiki directory (optional) (default: /home/USERNAME/vimwiki/)
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        absolute path to output directory (optional) (default: PROJECT_DIR/converted_files/)
```

## Goals:
 - Make it easier to migrate over existing VimWiki files to `.org` files
 - Have a *reasonable* amount `.wiki` file content converted to it's `.org` equivalent (**at least** 60-70%) so there's less to manually edit.
 
## Features:

**Extend for your own situation:**
 - The current config should be *good enough* for most basic VimWiki markdown, but **everyone's notes are different**.
 - Configure the [regex](./vimwiki_to_org/src/converters/helpers/wiki_regex.py) and the [markdown replacements](./vimwiki_to_org/src/converters/helpers/org_markdown.py) for your specific situation.

**Your ~/vimwiki/ directory is safe:**
- Your `.wiki` files are **not modified**, just read.
- Regular files are not touched (`.png`, etc). **Those will have to be manually transferred**.

**Keep your linked pages:**
- Links between `.wiki` files are converted to link to their new `.org` pages.

```
[[SomeWikiPage]] -> [[file:SomeWikiPage.org]]
```

**Regex is applied by priority:**
- Headers, code blocks and links get handled first before converting text emphasis markdown
- This is to avoid accidentally converting things like:
  - underscores used in a code block to italic text: `some_var_name -> some/var/name`
  - file names with underscores converted to italic text: ```file:some_file_name.png -> file:some/file/name.png```
  - etc, etc.
