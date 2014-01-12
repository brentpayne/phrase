from phrase.phrase_dictionary import PhraseDictionary, convert_run_to_text, convert_to_merged_ids

__author__ = 'brentpayne'

from lettuce import *

@step('And phrases "(.*)"')
def setup_phrase_dictionary(step, text):
    pd = PhraseDictionary()
    for phrase in text.split(","):
        pd.add_phrase(phrase.split())
    world.phrase_dictionary = pd

@step('Given text "(.*)"')
def setup_text(step, text):
    world.text = text

@step('We get the phrased text "(.*)"')
def check_phrase_results(step, excepted_result):
    phrase_ids = convert_to_merged_ids(world.text.split(), world.phrase_dictionary)
    text = " ".join(convert_run_to_text(phrase_ids, phrase_dictionary=world.phrase_dictionary))
    assert(text == excepted_result)



