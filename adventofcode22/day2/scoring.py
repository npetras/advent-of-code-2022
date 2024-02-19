from enum import Enum


class Result(Enum):
    """The number of points awarded to each result"""
    WIN = 6
    DRAW = 3
    LOSS = 0
