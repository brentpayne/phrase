import random
from lettuce import step, world
from phrase.noun_phrase_dictionary import NounPhraseDictionary, exclude_ngram_filter
from phrase.phrase_generation import extend_phrase_dictionary

__author__ = 'brentpayne'

def almost_random_pos(token):
    pos = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'SYM', 'CD', 'VBG', 'FW', 'NP', 'VV', 'JUNK',)
    rv = pos[random.randint(0, len(pos)-1)]
    for sub in ('ersin', 'esti', 'onty', 'ython', 'ying', 'oly', 'r'):
        if sub in token:
            rv = 'NN'
    return rv

class PoSCorpusWrapper(object):
    def __init__(self, corpus):
        self.corpus = corpus

    def __iter__(self):
        return self

    def next(self):
        return [[(w, almost_random_pos(w)) for w in s] for s in self.corpus.next()]


@step(u'Run PoS over corpus')
def pos_corpus(step):
    prev_gen = world.corpus.generate
    def new_corpus_generate():
        return PoSCorpusWrapper(prev_gen())
    world.corpus.generate = new_corpus_generate

@step(u'Generate noun phrases')
def generate_common_phrases(step):
    world.pd = NounPhraseDictionary()
    phrase_detection_alogrithm = NounPhraseDictionary.generate_phrase_detection_function(min_token_count=3, max_phrases=5, exclude_ngram_filter=exclude_ngram_filter)

    for i in range(4):
        world.pd = extend_phrase_dictionary(world.corpus.generate(),
                                            phrase_detection_alogrithm,
                                            world.pd)

@step(u'The following noun phrases were identified:')
def check_phrase_existance(step):
    for data in step.hashes:
        tokens = data['phrase'].split()
        phrase = "_".join(tokens)
        pos_tokens = [(t, 'NN') for t in tokens]
        tmp = world.pd.process(pos_tokens)
        tmp2 = world.pd.compose([t for (t, p) in tmp])
        phrased = " ".join(tmp2)
        assert phrase == phrased