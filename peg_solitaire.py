class Game():
    def __init__(self):
        x = "x"
        self.playing_field = [
            [x, x, 1, 1, 1, x, x],
            [x, x, 1, 1, 1, x, x],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [x, x, 1, 1, 1, x, x],
            [x, x, 1, 1, 1, x, x],
        ]
