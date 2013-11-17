import pickle
from corpus import FileCorpus
from phrase_generation import generate_phrases

__author__ = 'brentpayne'


def main(folder, pkl_filename, options={}):
    corpus = FileCorpus()
    corpus.add_folder(folder)
    pd = generate_phrases(
        corpus
        , word_filter_num=1
        , phrase_filter_num=2
        , total_number_of_phrases=10 if 'phrase_count' not in options else int(options['phrase_count'])
        , colloc_num_per_round=3 if 'colloc_per_round' not in options else int(options['colloc_per_round'])
        , colloc_rounds=4
    )
    with open(pkl_filename, 'w') as fp:
        pickle.dump(pd, fp)


if __name__ == "__main__":
    import sys
    print sys.argv
    main(sys.argv[1], sys.argv[2])
