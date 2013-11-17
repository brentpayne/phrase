Feature: Find given phrases in text
    Given a line of text and a dictionary of phrases
    I want to return text with the phrases joined

    Scenario: Identify one phrase within one text line
       Given text "<text>"
       And phrases "<phrases>"
       We get the phrased text "<result>"

    Examples:
        | text | phrases | result |
        | The Monty Python Flying Circus | Monty Python | The Monty_Python Flying Circus |
        | The Monty Python Flying Circus | Monty Python Flying Circus | The Monty_Python_Flying_Circus |
        | The Monty Python Flying Circus | The Monty Python Flying | The_Monty_Python_Flying Circus |
        | The Monty Python Flying Circus | The Monty Python Flying Circus | The_Monty_Python_Flying_Circus |
        | The Monty Python Flying Circus | Monty Python, The Monty Python | The_Monty_Python Flying Circus |
        | The Monty Python Flying Circus | Monty Python, Monty, Python Flying | The Monty_Python Flying Circus |
