"""Reading of the file (input) for the problem"""

from typing import List

from day2.shapes import Shape, ShapeChoicePair


def extract_strategy_guide_from_input() -> List[ShapeChoicePair]:
    """
    Reads strategy guide which predicts the opponent's choice recommends corresponding shape choices for each round.
    The strategy guide in text form is converted to the desired format.
    round.
    :return: List of pairs of choices for each round of the tournament
    """
    with open("input", "r") as file:
        shape_choice_pairs = []

        for line in file:
            # opponent choice - 1st element, our choice - 2nd element
            line_without_newline = line.strip()
            shape_choices_str = line_without_newline.split(" ")
            shape_choices = ShapeChoicePair(determine_shape(shape_choices_str[0]),
                                            determine_shape(shape_choices_str[1]))
            shape_choice_pairs.append(shape_choices)
        return shape_choice_pairs


def determine_shape(shape_str_representation: str) -> Shape:
    """
    Uses the string representation of the shapes in the input to convert them to internal objects representing the
    corresponding shapes.
    :param shape_str_representation: the string representation of the shape in the input file
    :return: Shape object that corresponds to the shape_str_representation
    """
    match shape_str_representation:
        # A = Rock for predicted move, X = Rock for recommended move. Same pattern for other shapes.
        case "A" | "X":
            return Shape.ROCK
        case "B" | "Y":
            return Shape.PAPER
        case "C" | "Z":
            return Shape.SCISSORS
        case _:
            raise ValueError("Unrecognised value - does not correspond to a shape")


print(extract_strategy_guide_from_input())
