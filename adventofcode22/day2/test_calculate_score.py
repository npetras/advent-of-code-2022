import unittest

from day2.calculate_score import calculate_scores_using_strategy_guide
from day2.shapes import ShapeChoicePair, Shape


class TestCalculateScore(unittest.TestCase):
    def test_basic_scoring(self):
        """Three rounds"""
        strategy_guide = [ShapeChoicePair(predicted=Shape.ROCK, recommended=Shape.PAPER),
                          ShapeChoicePair(predicted=Shape.PAPER, recommended=Shape.ROCK),
                          ShapeChoicePair(predicted=Shape.SCISSORS, recommended=Shape.SCISSORS)]
        actual_score = calculate_scores_using_strategy_guide(strategy_guide)
        expected_score = 15
        self.assertEqual(expected_score, actual_score)


if __name__ == '__main__':
    unittest.main()
