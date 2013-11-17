from phrase_dictionary import PhraseDictionary
from nose.tools import eq_

__author__ = 'brentpayne'


def test_maximal_phrase_init():
    pd = PhraseDictionary([['Monty', 'Python']])
    val = PhraseDictionary.return_max_phrase(['Monty', 'Python'], 0, pd)
    eq_(val, (-1, 2))

def test_maximal_phrase_1():
    pd = PhraseDictionary()
    pd.add_phrase(['Monty', 'Python'])
    val = PhraseDictionary.return_max_phrase(['Monty', 'Python'], 0, pd)
    eq_(val, (-1, 2))


def test_maximal_phrase_1_set_id():
    pd = PhraseDictionary()
    pd.add_phrase(['Monty', 'Python'], "Hello")
    val = PhraseDictionary.return_max_phrase(['Monty', 'Python'], 0, pd)
    eq_(val, ("Hello", 2))



def test_maximal_phrase_2():
    pd = PhraseDictionary()
    pd.add_phrase(['Monty', 'Python'])
    val = PhraseDictionary.return_max_phrase(['The', 'Monty', 'Python'], 0, pd)
    eq_(val, (None, None))