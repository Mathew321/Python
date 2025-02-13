import unittest
from collections import Counter
from main import DiceGame

class TestDiceGameEvaluate(unittest.TestCase):
    def setUp(self):
        self.game = DiceGame()

    def evaluate_score(self, picked, expected_score):
        self.game.picked = picked
        self.assertEqual(self.game.evaluate(), expected_score)

    def test_single_scores(self):
        self.evaluate_score([1], 100)
        self.evaluate_score([5], 50)

    def test_straights(self):
        self.evaluate_score([1, 2, 3, 4, 5, 6], 1500)
        self.evaluate_score([1, 2, 3, 4, 5], 750)
        self.evaluate_score([2, 3, 4, 5, 6], 750)
        self.evaluate_score([3, 4, 5, 6], 500)
        self.evaluate_score([1, 2, 3, 4], 500)
        self.evaluate_score([2, 3, 4, 5], 500)

    def test_triplets(self):
        self.evaluate_score([1, 1, 1], 1000)
        self.evaluate_score([2, 2, 2], 200)
        self.evaluate_score([3, 3, 3], 300)
        self.evaluate_score([4, 4, 4], 400)
        self.evaluate_score([5, 5, 5], 500)
        self.evaluate_score([6, 6, 6], 600)

    def test_multipliers(self):
        self.evaluate_score([6, 6, 6, 6], 1200)
        self.evaluate_score([1, 1, 1, 1], 2000)
        self.evaluate_score([2, 2, 2, 2, 2], 600)

    def test_combinations(self):
        self.evaluate_score([6, 6, 6, 1], 700)
        self.evaluate_score([1, 1, 1, 6, 6, 6], 1600)

    def test_fouls(self):
        self.evaluate_score([1, 2, 4, 5], 0)
        self.evaluate_score([1, 1, 1, 2], 0)
        self.evaluate_score([6, 6, 6, 1, 5, 2], 0)

if __name__ == '__main__':
    unittest.main()
