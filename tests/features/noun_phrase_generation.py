from lettuce import step, world
from phrase.noun_phrase_dictionary import NounPhraseDictionary
from phrase.phrase_generation import generate_phrases, extend_phrase_dictionary

__author__ = 'brentpayne'


@step(u'Generate noun phrases')
def generate_common_phrases(step):
    world.pd = NounPhraseDictionary()
    for i in range(4):
        world.pd = extend_phrase_dictionary(world.corpus.generate(),
                                            NounPhraseDictionary.generate_phrase_detection_function(min_token_count=3, max_phrases=5),
                                            world.pd)
