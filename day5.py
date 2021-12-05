from collections import Counter
from pyperclip import copy
import utils


def get_lines():
    lines = utils.get_input(5)
    return [list(map(int, line.replace(' -> ', ',').split(','))) for line in lines]


def part1(lines):
    c = Counter()
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                c[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                c[(x, y1)] += 1

    return sum(val > 1 for val in c.values())


def part2(lines):
    c = Counter()
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                c[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                c[(x, y1)] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            direction = 1 if y2 > y1 else -1
            x, y = x1, y1
            while x <= x2:
                c[(x, y)] += 1
                x, y = x+1, y+direction
            assert y-direction == y2

    return sum(val > 1 for val in c.values())


if __name__ == '__main__':
    print(answer1 := part1(get_lines()))
    print(answer2 := part2(get_lines()))
    copy(answer2)
