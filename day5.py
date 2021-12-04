from pyperclip import copy
import utils


def get_lines():
    return utils.get_input(4)


def part1(lines):
    return 0


def part2(lines):
    return 0


if __name__ == '__main__':
    print(answer1 := part1(get_lines()))
    print(answer2 := part2(get_lines()))
    copy(answer2)
