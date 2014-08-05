import pickle
from .corpus import FileBackedDocumentCorpus

__author__ = 'brentpayne'


def main():
    import sys
    print sys.argv
    folder = sys.argv[1]
    pkl_filename = sys.argv[2]
    options = {}
    corpus = FileBackedDocumentCorpus()
    corpus.add_folder(folder)
    pd = generate_phrases(
        corpus
        , word_filter_num=5
        , phrase_filter_num=5
        , total_number_of_phrases=400 if 'phrase_count' not in options else int(options['phrase_count'])
        , colloc_num_per_round=300 if 'colloc_per_round' not in options else int(options['colloc_per_round'])
        , colloc_rounds=4
    )
    with open(pkl_filename, 'w') as fp:
        pickle.dump(pd, fp)


if __name__ == "__main__":
    main()
