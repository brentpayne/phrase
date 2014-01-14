from collections import Counter
from itertools import chain, imap
from pprint import pprint
import nltk
from phrase.phrase_dictionary import convert_run_to_text, convert_run_to_text_token_run
from phrase_dictionary import PhraseDictionary

__author__ = 'brentpayne'


def add_to_word_counts(line, wc):
    pass


def add_to_bigram_counts(line, bc):
    pass


def identify_merges(bc, wc):
    pass


def identify_deletes(word_counts):
    pass


def update_dictionary(dictionary, merges, deletes):
    pass

EXCLUDE_SET1 = (")","(",",","'","\"")
EXCLUDE_SET2 = (':',")","(",",","'","\"","-","a","on","the","!","?","of","n't","'re", "to")

def exclude_ngram_filter(w1,w2):
    return w2[1] not in ('NNP', 'NN', 'VBG', 'NNS', 'NNPS', 'FW', 'CD') or w2[0] in EXCLUDE_SET2 or w1[0] in EXCLUDE_SET1

def generate_phrases(corpus, word_filter_num=1, phrase_filter_num=2, total_number_of_phrases=10, colloc_num_per_round=3, colloc_rounds=4):
    """

    :param corpus:
    :param word_filter_num:
    :param phrase_filter_num:
    :param total_number_of_phrases: @TODO change to phrase_filter where we crop from the bottom instead of from the top
    :param colloc_num_per_round:
    :param colloc_rounds:
    :return:
    """
    #tokens = chain.from_iterable(imap(pos_tag, imap(wtk, chain.from_iterable(imap(stk, corpus)))))
    tokens = chain.from_iterable(chain.from_iterable(corpus))
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
        run_another_phase_generation_round(corpus, pd, phrase_filter_num, colloc_num_per_round)

    def count_phrase_tokens_only(pos_sent, pd, counts):
        #tokens = list(chain.from_iterable(imap(wtk, text)))
        #print pos_sent
        tokens = [posword[0] for posword in pos_sent]

        icurrent = 0
        id_run = []
        while icurrent < len(tokens):
            id, inext = PhraseDictionary.return_max_phrase(tokens, icurrent, pd)
            if id is not None:
                id_run.append(id)
                icurrent = inext
            else:
                icurrent += 1

        return counts.update(id_run)

    #phrase_counts = Counter()
    #map(lambda x: count_phrase_tokens_only(x, pd, phrase_counts), imap(stk, corpus))
    #map(lambda x: count_phrase_tokens_only(x, pd, phrase_counts), chain.from_iterable(corpus))

    #print('Selected phrases')
    #pprint([ (pd.get_phrase(item[0]), item) for item in collocation_finder.nbest(bigram_measures.chi_sq, colloc_num_per_round)])
    # pd_filtered = PhraseDictionary(imap(lambda phc: pd.get_phrase(phc[0]), phrase_counts.most_common(total_number_of_phrases)))

    return pd

def run_another_phase_generation_round(corpus, pd, filter_num, colloc_num):
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
    tokens = chain.from_iterable(imap(convert_to_phrase_tokens, corpus))

    collocation_finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
    collocation_finder.apply_freq_filter(filter_num)  # @TODO remove bottom X%, and tune on X
    collocation_finder.apply_ngram_filter(exclude_ngram_filter)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    phrases = collocation_finder.nbest(bigram_measures.chi_sq, colloc_num)
    print "another run phrases"
    map(pd.add_phrase, imap(lambda p: convert_run_to_text_token_run([p[0][0], p[1][0]], phrase_dictionary=pd), phrases))
    print "another run phrases Done"
    #pprint([convert_run_to_text(ph, phrase_dictionary=pd) for ph in phrase_runs])
    #print "another run phrases DUP"
    #pprint(phrase_runs)
    #map(pd.add_phrase, phrase_runs)




