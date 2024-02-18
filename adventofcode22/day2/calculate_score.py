from typing import List, Tuple

from read_file import extract_strategy_guide_from_input
from day2.scoring import Result
from day2.shapes import Shape, ShapeChoicePair


def calculate_scores_using_strategy_guide(strategy_guide: List[ShapeChoicePair]) -> int:
    total_score = 0
    for round_choice in strategy_guide:
        total_score += determine_round_score(round_choice)
    return total_score


def determine_round_score(round_choice: ShapeChoicePair) -> Tuple[int, int]:
    if round_choice.predicted == round_choice.recommended:
        return Result.DRAW.value + round_choice.recommended.value
    else:
        match round_choice:
            case (Shape.ROCK, Shape.SCISSORS):
                return Result.WIN.value + Shape.ROCK.value
            case (Shape.SCISSORS, Shape.PAPER):
                return Result.WIN.value + Shape.SCISSORS.value
            case (Shape.PAPER, Shape.ROCK):
                return Result.WIN.value + Shape.PAPER.value
            case _:
                return Result.LOSS.value + round_choice.recommended.value


if __name__ == "__main__":
    strategy_guide_main = extract_strategy_guide_from_input()
    score_using_guide = calculate_scores_using_strategy_guide(strategy_guide_main)
    print(score_using_guide)
