# LL(1) Parser for Simple Mathematical Expressions

This project implements a predictive recursive descent parser (LL(1)) for recognizing simple mathematical expressions. The parser is designed to handle basic arithmetic operations, including addition, subtraction, multiplication, and division, as well as parentheses for grouping.

## Project Structure

The project is organized as follows:

```
ll1-parser-python
├── src
│   ├── lexer.py          # Lexical analyzer that tokenizes input expressions
│   ├── grammar.py        # Defines the context-free grammar (CFG) for expressions
│   ├── first_follow.py    # Functions to compute FIRST and FOLLOW sets
│   ├── parse_table.py    # Constructs the LL(1) parsing table
│   ├── parser.py         # Implements the LL(1) parsing algorithm
│   └── main.py           # Entry point of the program
├── tests
│   ├── test_grammar.py   # Unit tests for grammar and FIRST/FOLLOW sets
│   └── test_parser.py    # Unit tests for the parser functionality
├── docs
│   └── diagramas
│       └── afd_final.md  # Mermaid diagram representing the final AFD for tokens
├── pyproject.toml        # Project configuration file
├── requirements.txt      # List of project dependencies
├── .gitignore            # Files and directories to ignore in version control
└── README.md             # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the parser, execute the following command:

```
python src/main.py
```

You will be prompted to enter a mathematical expression. The parser will analyze the input and display the results, including the syntax tree and any derivations.

## Examples

Here are some examples of valid expressions that the parser can recognize:

1. `3 + 5`
2. `(2 * 4) - 1`
3. `10 / (2 + 3)`

## Testing

To run the unit tests for the grammar and parser, use the following command:

```
pytest
```

This will execute all tests defined in the `tests` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.