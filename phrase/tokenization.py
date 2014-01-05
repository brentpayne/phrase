from nltk import word_tokenize, sent_tokenize

__author__ = 'brentpayne'

def convert_to_idruns(line, token2id):
    rv = []
    run = []
    for token in line:
        id = token2id.get(token, None)
        if id is not None:
            run.append(id)
        else: # id is None
            if len(run):
                rv.append(run)
                run = []
    if len(run):
        rv.append(run)
    return rv

def tokenize_text(text):
    rv = []
    for sent in sent_tokenize(text):
        rv.append(word_tokenize(sent))
    return rv

class SentenceIterator(object):

    def __init__(self, text_iterable):
        """
        Intializes the sentence iterable with an iterable over text documents.
        :param text_iterable: The text document list
        :return: An iterator that returns one sentence at a time
        """
        self.input = text_iterable

    def __iter__(self):
        return self.data()

    def data(self):
        for text in self.input:
            for sent in sent_tokenize(text):
                yield sent
        raise StopIteration
