import unittest
from statistics_service import StatisticsService, SortBy
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_service_has_correct_players(self):
        correct_players = [i.__str__() for i in PlayerReaderStub().get_players()]

        players = [i.__str__() for i in self.stats._players]

        self.assertEqual(correct_players, players)


    def test_search_returns_correct(self):
        name = "Semenko"
        found = self.stats.search(name)

        self.assertEqual(name, found.name)

    def test_search_returns_none_if_no_player(self):
        name = "Rölli"
        found = self.stats.search(name)

        self.assertEqual(None, found)
    
    def test_team_returns_correct_team(self):
        team = "PIT"
        found = self.stats.team(team)

        self.assertEqual("Lemieux", found[0].name)
    
    def test_ranking_works(self):
        correct = ["Gretzky", "Lemieux", "Yzerman"]

        found = [i.name for i in self.stats.top(2)]

        self.assertEqual(correct, found)

    def test_ranking_assists_works(self):
        correct = ["Gretzky", "Yzerman"]

        found = [i.name for i in self.stats.top(1,SortBy.ASSISTS)]

        self.assertEqual(correct, found)

    def test_ranking_goals_works(self):
        correct = ["Lemieux", "Yzerman"]

        found = [i.name for i in self.stats.top(1,SortBy.GOALS)]

        self.assertEqual(correct, found)


    def test_ranking_points_works(self):
        correct = ["Gretzky", "Lemieux", "Yzerman"]

        found = [i.name for i in self.stats.top(2, SortBy.POINTS)]

        self.assertEqual(correct, found)

