import unittest
import peg_solitaire

class TestPegSolitaire(unittest.TestCase):
    def test_default_game(self):
        game = peg_solitaire.Game()
        self.assertIsNotNone(game,msg="Game was not successfully initialized")
