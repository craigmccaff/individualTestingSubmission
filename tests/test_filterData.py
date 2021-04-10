import unittest
from unittest.mock import MagicMock
from functions import fakingData, filterData, filterDataAdapter, searchTeam


class TestFilterData(unittest.TestCase):

    def test_inputNameEqualsOutputName(self):
        self.assertEqual(fakingData.getRecentUserInput(), filterDataAdapter.filterTeamDataAdapter()[0])

    def test_errorHandlingTeamName(self):
        searchTeam.formattedSearchTeam = MagicMock(side_effect=["error", "blue"])
        self.assertTrue(filterData.filterTeamData(searchTeam.formattedSearchTeam(), "mostRecentTableQuery.csv"))

    def test_cantReturnHeadings(self):
        searchTeam.formattedSearchTeam = MagicMock(side_effect=["Team", "blue"])
        self.assertEqual(filterData.filterTeamData(searchTeam.formattedSearchTeam(), "mostRecentTableQuery.csv")[0], "blue")

    def test_lenListEqualsLenHeadings(self):
        self.assertEqual(len(filterDataAdapter.filterTeamDataAdapter()), len(filterDataAdapter.getHeadingsAdapter()))

    def test_headingsValues(self):
        self.assertEqual(filterDataAdapter.getHeadingsAdapter(),
                         ["Team", "Position", "Games Played", "Wins", "Draws", "Losses", "Goals Scored",
                          "Goals Conceded"])


if __name__ == '__main__':
    unittest.main()
