import unittest
from functions import searchTeam
from unittest.mock import MagicMock

class TestSearchTeam(unittest.TestCase):


    def test_searchTeamCAPS(self):
        searchTeam.setSearchTeam = MagicMock(return_value = "RED")
        self.assertEqual(searchTeam.formattedSearchTeam(), "red")


if __name__ == '__main__':
    unittest.main()
