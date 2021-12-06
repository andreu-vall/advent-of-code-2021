from pyperclip import copy
import utils


def get_lines():
    return utils.int_lines(1)


def part1(lines):
    count = 0
    for i in range(len(lines)-1):
        count += lines[i+1] > lines[i]
    return count


def part2(lines):
    count = 0
    for i in range(len(lines)-3):
        count += lines[i+3] > lines[i]
    return count


if __name__ == '__main__':
    print(answer1 := part1(get_lines()))
    print(answer2 := part2(get_lines()))
    copy(answer2)
