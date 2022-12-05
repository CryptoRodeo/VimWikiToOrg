# (Vim|Wiki)ToOrg 🦄
> Migration to Org mode, made a bit easier

**Convert this:**

```
= Header1 =
== Header2 ==
=== Header3 ===
==== Heading4 ====
===== Heading5 =====
====== Heading6 ======

*bold text*

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
[[some wiki.org][description for some wiki file]]

-  bullet list item 1
-  bullet list item 2
    1) numbered list item 1
    2) numbered list item 2

#+begin_src python
def greet(s):
    print("Hello, " + s)

#+end_src

| a table |  |
|---------|--|
|         |  |

[[file:./some-image.png]]

```

## Goals:
 - Make it easier to migrate over existing VimWiki files to Org files
 - Have a *reasonable* amount `.wiki` file content converted to it's `.org` equivalent (**at least** 60-70%) so you have less to manually edit.
 
## Features:

**Extend for your own situation:**
 - The current config should be *good enough* for most basic VimWiki markdown, but **everyone's notes are different**.
 - Add or configure the [regex](./vimwiki_to_org/src/converters/helpers/wiki_regex.py) and the [markdown replacements](./vimwiki_to_org/src/converters/helpers/org_markdown.py) to what suits your specific situation

**Your .wiki files are safe:**
- Your `.wiki` files are left alone and are **not modified**, just read
- All converted files are exported to the `converted_files` directory in the project directory

**Keep your linked pages:**
- `.wiki` files that linked to other `.wiki` files should be converted over, allowing you to still have your links between documents in the new `.org` files

### Common Issues:

**Conversion of italics is currently not supported**:
- VimWiki uses the following markdown for italic text: `_italic text_`
- underscores can exist in content such as VimWiki code blocks and, based on the current implementation, this can interfere with content being converted properly

**asterisks, asterisk list, code examples with aterisk...**:

- Because of how asterisks are used in org files, some content might not get converted.

Personal example:

This code block didn't get converted to an org code block because of the excess asterisks used:

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
