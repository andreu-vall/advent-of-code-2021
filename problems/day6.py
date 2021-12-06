from collections import Counter
from pyperclip import copy
import utils


def get_count(data, days):
    c = Counter(data)
    for _ in range(days):
        d = Counter({k - 1: v for k, v in c.items()})
        d[6] += d[-1]
        d[8] = d[-1]
        del d[-1]
        c = d
    return sum(c.values())


def part1(data):
    return get_count(data, 80)


def part2(data):
    return get_count(data, 256)


def get_data():
    return list(map(int, utils.get_input(6)[0].split(',')))


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
