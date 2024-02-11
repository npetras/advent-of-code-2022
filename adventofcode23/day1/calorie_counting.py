"""Day 1: Calorie Counting"""


def calculate_total_calories_from_input():
    """
    :return: list of elfs with the total calories for each one
    """
    with open("input", "r") as file:
        sum_of_calories = 0     # sum for the current elf
        elfs = []               # total calories for each elf
        for line in file:
            if line != "\n":
                sum_of_calories += int(line)
            else:
                # new lines indicate the next elf is coming up
                elfs.append(sum_of_calories)
                sum_of_calories = 0
        return elfs


def part1_find_elf_with_most_calories():
    """
    :return: The number of calories held by the elf with the most snacks (calories)
    """
    part1_elfs = calculate_total_calories_from_input()
    return max(part1_elfs)


def part2_find_top_three_elfs():
    part2_elfs = calculate_total_calories_from_input()
    part2_elfs.sort()
    return part2_elfs[0] + part2_elfs[1] + part2_elfs[2]


if __name__ == '__main__':
    print(f"The top elf is carrying: {part1_find_elf_with_most_calories()} calories")
    print(f"The top three elfs are carrying: {part2_find_top_three_elfs()} calories")
