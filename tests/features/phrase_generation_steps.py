from lettuce import step, world
from phrase.corpus import FileCorpusGenerator
from phrase.phrase_generation import generate_phrases
from units.helpers import convert_filename_into_data_file_path

__author__ = 'brentpayne'


@step(u'Given corpus:')
def given_corpus(step):
    world.corpus = FileCorpusGenerator()
    for input in step.hashes:
        if 'file' in input and input['file']:
            file = convert_filename_into_data_file_path(input['file'])
            world.corpus.append(file)
        if 'folder' in input and input['folder']:
            folder = convert_filename_into_data_file_path(input['folder'])
            world.corpus.add_folder(folder)



@step(u'Generate common phrases')
def generate_common_phrases(step):
    if step.hashes:
        data = step.hashes[0]
    else:
        data = {}
    world.pd = generate_phrases(
        world.corpus.generate
        , word_filter_num=1
        , phrase_filter_num=2
        , colloc_num_per_round=3 if 'colloc_per_round' not in data else int(data['colloc_per_round'])
        , colloc_rounds=4
    )

@step(u'The following phrases were identified:')
def check_phrase_existance(step):
    for data in step.hashes:
        phrase = data['phrase'].split()
        assert world.pd.contains_tokens(phrase)