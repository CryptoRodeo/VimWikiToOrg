from ..helpers.markdown_classifier import classify_markdown

def test_vimwiki_markdown_classification(markdown_with_classifiers):
    """
    Tests how vimwiki markdown is classified
    """
    for wiki_markdown, expected_markdown_type in markdown_with_classifiers.items():
        assert expected_markdown_type == classify_markdown(wiki_markdown)
