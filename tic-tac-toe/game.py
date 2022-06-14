from .board import Board
from .player import Player

class Game:
    def __init__(self) -> None:
        self.game_board = Board()
        self.player_one = None
        self.player_two = None