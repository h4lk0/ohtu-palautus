import unittest
from statistics import SortBy
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_constructor(self):
        players = self.statistics._players

        self.assertEqual(len(players), 5)

    def test_search_returns_player(self):
        player = self.statistics.search("Kurri")

        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_search_returns_no_false_positives(self):
        player = self.statistics.search("askndjas")

        self.assertFalse(player)

    def test_team_search(self):
        team = self.statistics.team("EDM")

        self.assertEqual(len(team), 3)

    def test_top_three(self):
        topThree = self.statistics.top(2)

        self.assertEqual(len(topThree), 3)

    def test_top_by_assists(self):
        best = self.statistics.top(1, SortBy.ASSISTS)

        self.assertEqual(best[1].name, "Yzerman")

    def test_top_by_points(self):
        best = self.statistics.top(2)

        self.assertEqual(best[1].name, "Lemieux")

    def test_top_by_goals(self):
        best = self.statistics.top(1, SortBy.GOALS)

        self.assertEqual(best[0].name, "Lemieux")