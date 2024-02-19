from enum import Enum
from collections import namedtuple


class Shape(Enum):
    """
    The type of shape chosen by the player, and the number of points that choice awards.
    The name shape was chosen since this game is usually played using your hands.
    """
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# represents a pair of shapes from the strategy guide
# each round has a predicted opponent shape and a recommended response
ShapeChoicePair = namedtuple("ShapeChoicePair", ["predicted", "recommended"])
