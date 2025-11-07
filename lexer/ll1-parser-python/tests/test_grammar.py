import unittest
from src.grammar import Grammar
from src.first_follow import FirstFollow

class TestGrammar(unittest.TestCase):

    def setUp(self):
        self.grammar = Grammar()
        self.first_follow = FirstFollow(self.grammar)

    def test_first_sets(self):
        first_sets = self.first_follow.compute_first_sets()
        expected_first_sets = {
            'E': {'NUM', '(', 'ADD', 'SUB'},
            'T': {'NUM', '(', 'ADD', 'SUB'},
            'F': {'NUM', '('}
        }
        self.assertEqual(first_sets, expected_first_sets)

    def test_follow_sets(self):
        follow_sets = self.first_follow.compute_follow_sets()
        expected_follow_sets = {
            'E': {'$', ')'},
            'T': {'$', ')', '+'},
            'F': {'$', ')', '+', '*'}
        }
        self.assertEqual(follow_sets, expected_follow_sets)

    def test_grammar_productions(self):
        productions = self.grammar.get_productions()
        expected_productions = {
            'E': ['E + T', 'E - T', 'T'],
            'T': ['T * F', 'T / F', 'F'],
            'F': ['( E )', 'NUM']
        }
        self.assertEqual(productions, expected_productions)

if __name__ == '__main__':
    unittest.main()