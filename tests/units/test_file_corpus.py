import os
from corpus import FileCorpus
from helpers import convert_filename_into_data_file_path

__author__ = 'brentpayne'


def test_can_open_mutliple_files_multiple_times():
    corpus = FileCorpus()
    corpus.append(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt"))
    corpus.append(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt"))
    assert len(corpus) == 2

    i = 0
    for text in corpus:
        i += 1
        with open(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt")) as fp:
            txt2 = "".join(fp)
            assert text == txt2
    assert i == 2


    i = 0
    for text in corpus:
        i += 1
        with open(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt")) as fp:
            assert text == "".join(fp)
    assert i == 2


