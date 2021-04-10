import unittest
from functions import FilterDataAdapter, GoalDifference


class TestGoalDifferenceCalculator(unittest.TestCase):

    def test_positiveGoalDifference(self):
        self.assertEqual(GoalDifference.goalDifferenceCalculator(2, 1), "Goal Difference: 1")

    def test_negativeGoalDifference(self):
        self.assertEqual(GoalDifference.goalDifferenceCalculator(1, 2), "Goal Difference: -1")

    def test_zeroGoalDifference(self):
        self.assertEqual(GoalDifference.goalDifferenceCalculator(0, 0), "Goal Difference: 0")

    def test_stringInput(self):
        self.assertEqual(GoalDifference.goalDifferenceCalculator("1", "2"), "Goal Difference: -1")

    def testFileData(self):
        data = FilterDataAdapter.filterTeamDataAdapter()
        self.assertTrue(GoalDifference.goalDifferenceCalculator(data[6], data[7]))


if __name__ == '__main__':
    unittest.main()
