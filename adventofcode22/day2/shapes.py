from enum import Enum
from collections import namedtuple


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


ShapeChoicePair = namedtuple("ShapeChoicePair", ["predicted", "recommended"])
