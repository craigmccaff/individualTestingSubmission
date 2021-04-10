import unittest
from functions import SearchTeam
from unittest.mock import MagicMock


class TestSearchTeam(unittest.TestCase):

    def test_searchTeamCAPS(self):
        SearchTeam.setSearchTeam = MagicMock(return_value="RED")
        self.assertEqual(SearchTeam.formattedSearchTeam(), "red")


if __name__ == '__main__':
    unittest.main()
