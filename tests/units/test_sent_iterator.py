from phrase.tokenization import SentenceIterator

__author__ = 'brentpayne'

def test_sent_iteration_over_single_doc():
    text = """This is a sentence. This is the next sentence."""
    si = SentenceIterator([text])
    for i, sent in enumerate(si):
        if i == 0:
            assert sent == "This is a sentence."
        elif i == 1:
            assert sent == "This is the next sentence."