from collections import Counter
from itertools import chain, imap
from pprint import pprint
import nltk
from phrase.noun_phrase_dictionary import exclude_ngram_filter
from phrase.phrase_dictionary import convert_run_to_text, convert_run_to_text_token_run
from phrase_dictionary import PhraseDictionary

__author__ = 'brentpayne'

def extend_phrase_dictionary(corpus, phrase_discovery_function, phrase_dictionary):
    """

    :param corpus: a corpus of document of sentences of tokens.
    So an iterable of iterables of iterables of tokens : corpus of files of sentences of tokens
     Or, restated, a list of sentences each split into tokens.
    :param phrase_function: a function that takes a corpus of tokens returns phrases.
     The return value is a list of lists with the interal lists being an ordered list of tokens.
     The ordered list represents a single phrase.
    :param phrase_dictionary: a PhraseDictionary or other type that implements both :func:`add` and :func:`process`
    :return: returns a phrase_dictionary
    """
    sentences = chain.from_iterable(corpus)
    tokens = chain.from_iterable(imap(phrase_dictionary.process, sentences))
    phrases = phrase_discovery_function(tokens)
    map(phrase_dictionary.add, (phrase_dictionary.decompose(ph) for ph in phrases))
    return phrase_dictionary



def generate_phrases(corpus_func, word_filter_num=1, phrase_filter_num=2, colloc_rounds=4, colloc_num_per_round=3):
    """

    :param corpus_func: a function that returns an iterable to a corpus
    :param word_filter_num: the minimum number of times a word needs to appear to be considered
    :param phrase_filter_num: the minimum number of times a phrase needs to appear to be considered
    :param colloc_rounds: number of collocation rounds
    :param colloc_num_per_round: number of ngrams to join per round of collocation
    :return:
    """
    #tokens = chain.from_iterable(imap(pos_tag, imap(wtk, chain.from_iterable(imap(stk, corpus)))))
    tokens = chain.from_iterable(chain.from_iterable(corpus_func()))
    collocation_finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
    print ("here")
    collocation_finder.apply_freq_filter(word_filter_num)  # @TODO remove bottom X%, and tune on X
    #collocation_finder.apply_ngram_filter(lambda w1, w2: w2[1] not in ('NNP', 'NN') or w2[0] in EXCLUDE_SET)
    collocation_finder.apply_ngram_filter(exclude_ngram_filter)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    phrases = collocation_finder.nbest(bigram_measures.chi_sq, colloc_num_per_round)
    print('first phrases', phrases)
    pprint(phrases)

    pd = PhraseDictionary([[p[0][0], p[1][0]] for p in phrases])
    for i in xrange(colloc_rounds-1):
        run_another_phase_generation_round(corpus_func, pd, phrase_filter_num, colloc_num_per_round)

    return pd

def run_another_phase_generation_round(corpus_func, pd, filter_num, colloc_num):
    """

    :param corpus_func:
    :param pd:
    :param filter_num:
    :param colloc_num:
    :return:
    """
    def convert_to_phrase_tokens(pos_tokens):
        #pos_tokens = imap(pos_tag, imap(wtk, text))
        poses = []
        tokens = []
        for tk, pos in chain.from_iterable(pos_tokens):
            poses.append(pos)
            tokens.append(tk)

        icurrent = 0
        id_run = []
        while icurrent < len(tokens):
            id, inext = PhraseDictionary.return_max_phrase(tokens, icurrent, pd)
            if id is not None:
                id_run.append((id, poses[inext-1]))
                icurrent = inext
            else:
                id_run.append((tokens[icurrent], poses[icurrent]))
                icurrent += 1

        return id_run

    #tokens = chain.from_iterable(imap(convert_to_phrase_tokens, imap(stk, corpus)))
    tokens = chain.from_iterable(imap(convert_to_phrase_tokens, corpus_func()))

    collocation_finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
    collocation_finder.apply_freq_filter(filter_num)  # @TODO remove bottom X%, and tune on X
    collocation_finder.apply_ngram_filter(exclude_ngram_filter)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    phrases = collocation_finder.nbest(bigram_measures.chi_sq, colloc_num)
    print "another run phrases"
    map(pd.add, imap(lambda p: convert_run_to_text_token_run([p[0][0], p[1][0]], phrase_dictionary=pd), phrases))
    print "another run phrases Done"





