Feature: Identify phrases in a corpus
    Given a bunch of text, possibly spread across files
    Identify and return common phrases

    Scenario: Identify noun phrases from a file
        Given corpus:
            | file |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
        Run PoS over corpus
        Generate noun phrases
        The following noun phrases were identified:
            | phrase |
            | The Monty Python Flying Circus |


    Scenario: Identify yersinia pestis as a noun phrase from pubmed articles
        Given corpus:
            | folder |
            | yersinia |
        Run PoS over corpus
        Generate noun phrases:
            | phrase_count | colloc_per_round |
            | 50 | 50 |
        The following noun phrases were identified:
            | phrase |
            | Yersinia pestis |


