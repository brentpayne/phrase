__author__ = 'brentpayne'


class WordList(dict):
    def __init__(self):
        self.id2word = {}
        self.next_id = 1
    # cannot pickle generators
    #     self.word_id_gen = self.word_id_generator()
    #
    # def word_id_generator(self):
    #     """
    #     A generator for automatically labeling the next added word.
    #     Word IDs are positive by convention, as Phrase IDs are negative by convention.
    #     This is make it easy to extend and mix word ids and phrase ids without using the class system.
    #     :return: the next negative phrase ID
    #     """
    #     id = 0
    #     while True:
    #         id += 1
    #         yield id

    def get_next_id(self):
        rv = self.next_id
        self.next_id += 1
        return rv

    def add(self, word, id=None):
        """
        Adds a new word to the WordList and assigns it an id.  If id is set,
        :param word: The word token
        :param id: (Optional) The token id can be set, but bypasses the automatic id assignment.  Only specify the id
          if you plan to specify it on all add calls.
        :return: None
        """
        word_id = id if id is not None else self.get_next_id()
        self[word] = word_id
        self.id2word[word_id] = word

    def contains(self, id):
        """
        Determines if an ID is part of the word lis
        :param id: the id to check
        :return: True if the id is in the word list
        """
        return id in self.id2word
