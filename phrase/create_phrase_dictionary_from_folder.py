from collections import Counter
import pickle
from pprint import pprint
from phrase.corpus import FileCorpus
from phrase.phrase_generation import generate_phrase_dictionary

__author__ = 'brentpayne'


def main():
    import sys
    print sys.argv
    folder = sys.argv[1]
    pkl_filename = sys.argv[2]
    options = {}
    corpus = FileCorpus()
    corpus.add_folder(folder)
    phrase_dictionary = generate_phrase_dictionary(
        corpus.get_iterator
    )
    counts = Counter()
    with open(pkl_filename, 'w') as fp:
        pickle.dump(phrase_dictionary, fp)
    for doc in corpus.get_iterator():
        for line in doc:
            run = phrase_dictionary.process(line)
            for token_id in run:
                if token_id < 0:
                    counts[token_id] += 1

    pprint([phrase_dictionary.get_phrase(token_id) for (token_id, _) in counts.most_common(25)])


if __name__ == "__main__":
    main()
