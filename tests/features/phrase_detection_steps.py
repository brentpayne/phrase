from phrase.phrase_dictionary import PhraseDictionary, convert_run_to_text

__author__ = 'brentpayne'

from lettuce import *

@step('And phrases "(.*)"')
def setup_phrase_dictionary(step, text):
    pd = PhraseDictionary()
    for phrase in text.split(","):
        pd.add(phrase.split())
    world.phrase_dictionary = pd

@step('Given text "(.*)"')
def setup_text(step, text):
    world.text = text

@step('We get the phrased text "(.*)"')
def check_phrase_results(step, excepted_result):
    phrase_ids = world.phrase_dictionary.process(world.text.split())
    text = " ".join(convert_run_to_text(phrase_ids, phrase_dictionary=world.phrase_dictionary))
    assert(text == excepted_result)



