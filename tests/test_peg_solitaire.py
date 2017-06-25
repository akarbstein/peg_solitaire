import unittest
import peg_solitaire


class TestPegSolitaire(unittest.TestCase):
    def test_default_game(self):
        game = peg_solitaire.Game()
        self.assertIsNotNone(game, msg="Game was not successfully initialized")
        # After initialization the playing field should be initialized like that:
        x = "x"
        playing_field = [
            [x, x, 1, 1, 1, x, x],
            [x, x, 1, 1, 1, x, x],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [x, x, 1, 1, 1, x, x],
            [x, x, 1, 1, 1, x, x],
        ]
        self.assertEqual(game.playing_field(),playing_field,msg="Playing field not correctly initialized")
