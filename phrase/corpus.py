import os

__author__ = 'brentpayne'


class FileCorpus(list):
    def __init__(self, *files):
        """
        Initializes the FileCorpus with a list of files.
        :param files: a list of filepaths
        :return: None
        """
        self.extend(files)
        self.idx = -1

    def add_folder(self, folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            self.extend([os.path.join(root, name) for name in files])

    def reset(self):
        self.idx = -1

    def __iter__(self):
        return self

    def next(self):
        for filepath in self:
            with open(filepath) as fp:
                for line in fp:
                    yield line


class CorpusGenerator(FileCorpus):
    def __init__(self, cls, *files):
        """
        Initializes the FileCorpus with a list of files.
        :param cls: the cls type to generate
        :param files: a list of filepaths
        :return: None
        """
        self.cls = cls
        self.extend(files)

    def generate(self):
        return self.cls(*self)

    def __iter__(self):
        return self

    def next(self):
        return self.generate()

