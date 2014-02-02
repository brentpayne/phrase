from lettuce import step, world
from phrase.corpus import CorpusGenerator, FileCorpus
from phrase.phrase_dictionary import PhraseDictionary
from phrase.phrase_generation import extend_phrase_dictionary
from units.helpers import convert_filename_into_data_file_path

__author__ = 'brentpayne'


@step(u'Given corpus:')
def given_corpus(step):
    files = []
    fc = FileCorpus()
    for input in step.hashes:
        if 'file' in input and input['file']:
            file = convert_filename_into_data_file_path(input['file'])
            fc.append(file)
        if 'folder' in input and input['folder']:
            folder = convert_filename_into_data_file_path(input['folder'])
            fc.add_folder(folder)
    world.corpus = CorpusGenerator(FileCorpus, *fc.files)



@step(u'Generate common phrases')
def generate_common_phrases(step):
    world.pd = PhraseDictionary()
    for i in range(4):
        world.pd = extend_phrase_dictionary(world.corpus.generate(),
                                            PhraseDictionary.generate_phrase_detection_function(min_token_count=3, max_phrases=5),
                                            world.pd)


@step(u'The following phrases were identified:')
def check_phrase_existance(step):
    for data in step.hashes:
        tokens = data['phrase'].split()
        phrase = "_".join(tokens)
        phrased = " ".join(world.pd.compose(world.pd.process(tokens)))
        assert phrase == phrased