from itertools import imap, chain
import pickle
from gensim.models import Word2Vec
from nltk import pos_tag, word_tokenize as wtk, sent_tokenize as stk
from corpus import FileCorpus
from phrase.phrase_dictionary import convert_run_to_text, convert_to_merged_ids
from phrase_generation import generate_phrases


__author__ = 'brentpayne'


def main(foobar, folder, phrase_pkl, model_filename):
    corpus = FileCorpus()
    corpus.add_folder(folder)

    with open(phrase_pkl, 'r') as fp:
        pd = pickle.load(fp)

    def translate_into_phrase(tk_run):
        merged_ids = convert_to_merged_ids(tk_run, pd)
        merged_tokens = convert_run_to_text(merged_ids, phrase_dictionary=pd)
        return merged_tokens
    sentences = imap(translate_into_phrase, imap(wtk, chain.from_iterable(imap(stk, corpus))))
    model = Word2Vec(sentences, size=10000, window=7, min_count=4, workers=4)
    model.save(model_filename)

if __name__ == "__main__":
    import sys
    print sys.argv
    main(*sys.argv)
