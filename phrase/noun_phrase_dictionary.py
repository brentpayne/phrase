from copy import copy
from itertools import imap, chain
from phrase.phrase_dictionary import PhraseDictionary, convert_run_to_text
from word_list import WordList

__author__ = 'brentpayne'


class NounPhraseDictionary(PhraseDictionary):
    """
    The phrase dictionary contains sequences of identified phrases as a sequence of tokens.  It can be used to convert
    a string of tokens into a phrase id.  Phrase ids
    """


    def merge_pos_tokens(self, pos_tokens):
        """
        takes an array of Part of Speech labeled tokens and returns a set of tokens where word tokens have been merged into Noun phrases.
        :param pos_tokens: an array of (token, POS)
        :returns: returns an array of word and phrase tokens
        """
        if pos_tokens is None or len(pos_tokens)<0:
            return ""
        tokens, pos = zip(*pos_tokens)
        pos_phrase_ids = self.convert_noun_phrases(tokens, pos)
        phrase_ids, phrase_pos = zip(*pos_phrase_ids)
        phrase_text = convert_run_to_text(phrase_ids, phrase_dictionary=self)
        return zip(phrase_text, phrase_pos)


    def convert_noun_phrases(self, id_run, pos_run):
        """
        Converts any identified phrases in the run into phrase_ids.  The dictionary provides all acceptable phrases
        :param id_run: a run of token ids
        :param dictionary: a dictionary of acceptable phrases described as there component token ids
        :return: a run of token and phrase ids.
        """
        i = 0
        rv = []
        while i < len(id_run):
            phrase_id, offset = PhraseDictionary.return_max_phrase(id_run, i, self)
            if phrase_id:
                if pos_run[i] in ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'SYM', 'CD', 'VBG', 'FW', 'NP'):
                    print "MERGED", pos_run[i], self.get_phrase(phrase_id)
                    rv.append((phrase_id,'NP'))
                    i = offset
                else:
                    print "SKIPPED", pos_run[i], self.get_phrase(phrase_id)
                    rv.append((id_run[i], pos_run[i]))
                    i += 1
            else:
                rv.append((id_run[i], pos_run[i]))
                i += 1
        return rv

    def add(self, phrase, id=None):
        """
        Adds a new phrase to the dictionary
        :param phrase: the new phrase as a list of tokens
        :param phrase_id: optionally the phrase_id can be set on addition.  Beware, if you set one id you should set
            them all as the auto-generated ids do not take into account phrase_ids set this way.
        :return: None
        """
        if len(phrase) > 0 and type(phrase[0]) in (tuple, list):
            phrase = [token[0] for token in phrase]
        super(NounPhraseDictionary, self).add(phrase, id)

    def process(self, tokens):
        pos_tokens = []
        text_tokens = []
        for tk, pos in tokens:
            pos_tokens.append(pos)
            text_tokens.append(tk)

        icurrent = 0
        id_run = []
        while icurrent < len(text_tokens):
            id, inext = self.max_phrase(text_tokens, icurrent)
            if id is not None:
                id_run.append((id, pos_tokens[inext-1]))
                icurrent = inext
            else:
                id_run.append((text_tokens[icurrent], pos_tokens[icurrent]))
                icurrent += 1

        return id_run

    def decompose(self, id_run):
        toks = []
        for tok, pos in id_run:
            toks.append(tok)
        return super(NounPhraseDictionary, self).decompose(toks)


EXCLUDE_SET1 = (")","(",",","'","\"")
EXCLUDE_SET2 = (':',")","(",",","'","\"","-","a","on","the","!","?","of","n't","'re", "to")


def exclude_ngram_filter(w1,w2):
    if type(w1) in (tuple,list):
        return w2[1] not in ('NNP', 'NN', 'VBG', 'NNS', 'NNPS', 'FW', 'CD')\
                   or w2[0] in EXCLUDE_SET2 or w1[0] in EXCLUDE_SET1
    else:
        return False

