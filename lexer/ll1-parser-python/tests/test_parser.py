import unittest
from src.parser import Parser
from src.lexer import Lexer

class TestParser(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def test_simple_expression(self):
        tokens = self.lexer.tokenize("3 + 5")
        result = self.parser.parse(tokens)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 8)

    def test_expression_with_parentheses(self):
        tokens = self.lexer.tokenize("(2 + 3) * 4")
        result = self.parser.parse(tokens)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 20)

    def test_expression_with_precedence(self):
        tokens = self.lexer.tokenize("2 + 3 * 4")
        result = self.parser.parse(tokens)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 14)

    def test_invalid_expression(self):
        tokens = self.lexer.tokenize("3 + * 5")
        with self.assertRaises(SyntaxError):
            self.parser.parse(tokens)

    def test_empty_expression(self):
        tokens = self.lexer.tokenize("")
        with self.assertRaises(SyntaxError):
            self.parser.parse(tokens)

if __name__ == '__main__':
    unittest.main()