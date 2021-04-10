import unittest
from unittest.mock import MagicMock
from functions import fakingData, filterData, filterDataAdapter, searchTeam


class TestFilterData(unittest.TestCase):

    def test_inputNameEqualsOutput(self):
        self.assertEqual(fakingData.getRecentUserInput(), filterDataAdapter.filterDataAdapter()[0])

    def test_errorHandling(self):
        searchTeam.formattedSearchTeam = MagicMock(side_effect=["error", "blue"])
        self.assertTrue(filterData.filterData(searchTeam.formattedSearchTeam(), "mostRecentTableQuery.csv"))

    def test_lenListEqualsHeadings(self):
        self.assertEqual(len(filterDataAdapter.filterDataAdapter()), len(filterDataAdapter.getHeadingsAdapter()))


if __name__ == '__main__':
    unittest.main()
