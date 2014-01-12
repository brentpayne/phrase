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
        self.idx += 1
        try:
            print "opening", self[self.idx]
            with open(self[self.idx]) as fp:
                txt = "".join(fp)
            print "text", txt
            return txt
        except IndexError as _:
            self.reset()
            raise StopIteration

