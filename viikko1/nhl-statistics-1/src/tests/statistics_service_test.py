import unittest
from statistics_service import StatisticsService
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

    # ...
    def test_find_player_name(self):
        res = self.stats.search("Lemieux").goals
        self.assertEqual(res, 45)
    
    def test_find_none_by_name(self):
        self.assertEqual(self.stats.search("kummitus"), None)
    
    def test_team_search(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
    
    def test_top_players(self):
        tops = self.stats.top(2)

        self.assertEqual(tops[0].name, "Gretzky")
        self.assertEqual(tops[1].name, "Lemieux")