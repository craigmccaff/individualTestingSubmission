import unittest
from functions import PointsCalculator, FilterDataAdapter


class TestPointsCalculator(unittest.TestCase):

    def test_wins(self):
        self.assertEqual(PointsCalculator.pointsCalculator(1, 0), "Points Total: 3")

    def test_draws(self):
        self.assertEqual(PointsCalculator.pointsCalculator(0, 1), "Points Total: 1")

    def test_winsAndDraws(self):
        self.assertEqual(PointsCalculator.pointsCalculator(1, 1), "Points Total: 4")

    def test_zeroWinsOrDraws(self):
        self.assertEqual(PointsCalculator.pointsCalculator(0, 0), "Points Total: 0")

    def test_stringInput(self):
        self.assertEqual(PointsCalculator.pointsCalculator("3", "2"), "Points Total: 11")

    def test_fileData(self):
        data = FilterDataAdapter.filterTeamDataAdapter()
        self.assertTrue(PointsCalculator.pointsCalculator(data[3], data[4]))


if __name__ == '__main__':
    unittest.main()
