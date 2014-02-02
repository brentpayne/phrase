import os

__author__ = 'brentpayne'


class FileCorpus(object):
    def __init__(self, *files):
        """
        Initializes the FileCorpus with a list of files.
        :param files: a list of filepaths
        :return: None
        """
        self.files = []
        self.files.extend(files)
        self.idx = -1

    def extend(self, *files):
        self.files.extend(files)

    def append(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            self.files.extend([os.path.join(root, name) for name in files])

    def reset(self):
        self.idx = -1

    def __iter__(self):
        return self

    def next(self):
        self.idx += 1
        if self.idx >= len(self.files):
            self.idx = -1
            raise StopIteration
        filepath = self.files[self.idx]
        file_lines = []
        with open(filepath) as fp:
            for line in fp:
                file_lines.append(line.split())
        return file_lines




class CorpusGenerator(FileCorpus):
    def __init__(self, cls, *args):
        """
        Initializes the FileCorpus with a list of files.
        :param cls: the cls type to generate
        :param files: a list of filepaths
        :return: None
        """
        self.cls = cls
        self.args = args

    def generate(self):
        return self.cls(*self.args)

    def __iter__(self):
        return self

    def next(self):
        return self.generate()

