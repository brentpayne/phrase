Phrase
======

A library that builds on nltk and gensim to automatically generate phrases.


Installation
============

Add the package to your python path using pip:

```bash
pip install phrase
```

Usage
=====

To create a phrase dictionary and print out the top 25 phrases:

```bash
create_phrase_dictionary <corpus_folder> <phrase_dictionary_output_filename>
```

This is not a light process, it can take a lot of memory and time, so be warned.

Tests
=====

To run all the tests, you need to run py.test to pick up the unit tests.  Lettuce is currently being used for BDD tests
and needs to be run from the tests folder or with tests/ added to the PYTHONPATH (the tests utilize the units.helpers modules)
```bash
py.test
PYTHONPATH=tests lettuce tests/features
cd tests
lettuce features/
```