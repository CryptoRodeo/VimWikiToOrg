# (Vim|Wiki)ToOrg 🦄
> Migration to Org mode, made a bit easier

## Goals:
 - Make it easier to migrate over existing VimWiki files to Org files
 - Have a *reasonable* amount of VimWiki markup converted to it's Org mode equivalent (**at least** 60-70%)
 
## Features:

**Extend for your own situation:**
 - The current config should be *good enough* for most basic VimWiki markdown, but **everyone's notes are different**.
 - Add or configure the regex and the markdown replacements to what suits your specific situation

**Your .wiki files are safe:**
- Your `.wiki` files are left alone and are **not modified**, just read
- All converted files are exported to the `converted_files` directory in the project directory

**Keep your linked pages:**
- `.wiki` files that linked to other `.wiki` files should be converted over, allowing you to still have your links between documents in the new `.org` files
