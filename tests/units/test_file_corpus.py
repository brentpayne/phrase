from phrase.corpus import FileCorpus
from helpers import convert_filename_into_data_file_path

__author__ = 'brentpayne'


def test_can_open_multiple_files_multiple_times():
    corpus = FileCorpus()
    corpus.append(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt"))
    corpus.append(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt"))
    assert len(corpus.files) == 2

    documents = corpus.get_iterator()
    i = 0
    for file_data in documents:
        i += 1
        file_data = list(file_data)
        with open(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt")) as fp:
            for j, line in enumerate(fp):
                txt = " ".join(file_data[j])
                assert txt == line.strip()
    assert i == 2

    documents = corpus.get_iterator()
    i = 0
    for file_data in documents:
        i += 1
        file_data = list(file_data)
        with open(convert_filename_into_data_file_path("the_monty_python_flying_circus.txt")) as fp:
            for j, line in enumerate(fp):
                txt = " ".join(file_data[j])
                assert txt == line.strip()
    assert i == 2




