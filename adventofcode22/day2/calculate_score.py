from typing import List

from read_file import extract_strategy_guide_from_input
from day2.scoring import Result
from day2.shapes import Shape, ShapeChoicePair


def calculate_scores_using_strategy_guide(strategy_guide: List[ShapeChoicePair]) -> int:
    """
    Based on the strategy guide determine what score would be achieved in the tournament.
    :param strategy_guide: list of rounds with predicted opponent shape choice and recommended option, the recommended
    move will not always be a win to avoid suspicion
    :return: total score in the tournament based on rounds described in the strategy guide
    """
    total_score = 0
    for round_choice in strategy_guide:
        total_score += determine_round_score(round_choice)
    return total_score


def determine_round_score(round_choices: ShapeChoicePair) -> int:
    """
    Determines the score for each round by determining if it is a win, loss or draw; and adding points based on the
    shape chosen -- each choice awards a certain number of points.
    :param round_choices: the predicted oponent shape choice and recommended choice in response
    :return: the score awarded for that round based in round_choices
    """
    # draw
    if round_choices.predicted == round_choices.recommended:
        return Result.DRAW.value + round_choices.recommended.value
    else:
        match round_choices:
            # predicted is first, then recommended choice
            # scissors loses to rock
            case (Shape.SCISSORS, Shape.ROCK):
                return Result.WIN.value + Shape.ROCK.value
            # paper loses to scissors
            case (Shape.PAPER, Shape.SCISSORS):
                return Result.WIN.value + Shape.SCISSORS.value
            # rocks loses to paper
            case (Shape.ROCK, Shape.PAPER):
                return Result.WIN.value + Shape.PAPER.value
            # loss
            case _:
                return Result.LOSS.value + round_choices.recommended.value


if __name__ == "__main__":
    strategy_guide_main = extract_strategy_guide_from_input()
    score_using_guide = calculate_scores_using_strategy_guide(strategy_guide_main)
    print(score_using_guide)
