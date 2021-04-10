import unittest
from unittest.mock import MagicMock
from functions import FakingData, FilterData, FilterDataAdapter, SearchTeam


class TestFilterData(unittest.TestCase):

    def test_inputNameEqualsOutputName(self):
        self.assertEqual(FakingData.getRecentUserInput(), FilterDataAdapter.filterTeamDataAdapter()[0])

    def test_errorHandlingTeamName(self):
        SearchTeam.formattedSearchTeam = MagicMock(side_effect=["error", "blue"])
        self.assertTrue(FilterData.filterTeamData(SearchTeam.formattedSearchTeam(), "MostRecentTableQuery.csv"))

    def test_cantReturnHeadings(self):
        SearchTeam.formattedSearchTeam = MagicMock(side_effect=["Team", "blue"])
        self.assertEqual(FilterData.filterTeamData(SearchTeam.formattedSearchTeam(), "MostRecentTableQuery.csv")[0], "blue")

    def test_lenListEqualsLenHeadings(self):
        self.assertEqual(len(FilterDataAdapter.filterTeamDataAdapter()), len(FilterDataAdapter.getHeadingsAdapter()))

    def test_returnHeadingsValues(self):
        self.assertEqual(FilterDataAdapter.getHeadingsAdapter(),
                         ["Team", "Position", "Games Played", "Wins", "Draws", "Losses", "Goals Scored",
                          "Goals Conceded"])


if __name__ == '__main__':
    unittest.main()
