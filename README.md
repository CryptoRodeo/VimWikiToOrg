# (Vim|Wiki)ToOrg 🦄
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

[[wiki_link]]
[[some_wiki|description for some wiki file]]

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

[[file:wiki_link.org]]
[[some_wiki.org][description for some wiki file]]

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

### Common Issues:

**Conversion of italics is currently not supported**:
- VimWiki uses the following markdown for italic text: `_italic text_`.
- underscores can exist in content such as VimWiki code blocks and, based on the current implementation, this can interfere with content conversion.

**asterisks, asterisk list items, code examples with asterisks...**:

- Because of how asterisks are used in org files, some content might not get converted.

Personal example:

This code block in one of my files didn't get converted to an org code block because of the excess asterisks used in it:

```
{{{bash
# crontab examples:
* * * * * command # run command every minute
* 30 7 * * * command # run command at 7:30 everyday
* 30 7 5 * * command # run command at 7:30 the 5th day of every month
* 30 7 5 1 * command # run the command at 7:30 every january 5
* 30 7 * * 1 command # run the command at 7:30 every monday
}}}
```
