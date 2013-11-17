import os

__author__ = 'brentpayne'


def convert_filename_into_data_file_path(filename):
    return os.path.join(os.path.dirname(__file__), os.path.join("../data", filename))