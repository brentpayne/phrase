from lettuce import step, world
from phrase.corpus import CorpusGenerator
from phrase.phrase_dictionary import PhraseDictionary
from phrase.phrase_generation import generate_phrases, extend_phrase_dictionary
from units.helpers import convert_filename_into_data_file_path

__author__ = 'brentpayne'


@step(u'Given corpus:')
def given_corpus(step):
    world.corpus = CorpusGenerator()
    for input in step.hashes:
        if 'file' in input and input['file']:
            file = convert_filename_into_data_file_path(input['file'])
            world.corpus.append(file)
        if 'folder' in input and input['folder']:
            folder = convert_filename_into_data_file_path(input['folder'])
            world.corpus.add_folder(folder)



@step(u'Generate common phrases')
def generate_common_phrases(step):
    world.pd = PhraseDictionary()
    for i in range(4):
        world.pd = extend_phrase_dictionary(world.corpus.generate(),
                                            PhraseDictionary.generate_phrase_detection_function(min_token_count=1, max_phrases=3),
                                            world.pd)


@step(u'The following phrases were identified:')
def check_phrase_existance(step):
    for data in step.hashes:
        phrase = data['phrase'].split()
        assert world.pd.contains_tokens(phrase)