Feature: Identify phrases in a corpus
    Given a bunch of text, possibly spread across files
    Identify and return common phrases

    Scenario: Identify phrase from a file
        Given corpus:
            | file |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
            | the_monty_python_flying_circus.txt |
        Generate common phrases
        The following phrases were identified:
            | phrase |
            | Monty Python Flying Circus |


    Scenario: Identify yersinia pestis from pubmed articles
        Given corpus:
            | folder |
            | yersinia |
        Generate common phrases:
            | phrase_count | colloc_per_round |
            | 50 | 10 |
        The following phrases were identified:
            | phrase |
            | Yersinia pestis |


