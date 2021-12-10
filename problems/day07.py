from pyperclip import copy
import utils
import numpy as np


def part1(data):
    min_cost = float('inf')
    for v in set(data):
        cost = np.sum(np.abs(np.array(data)-v))
        min_cost = min(min_cost, cost)
    return min_cost


def part2(data):
    min_cost = float('inf')
    for v in range(min(data), max(data)+1):
        cost = 0
        for vv in data:
            n = abs(v - vv)
            cost += n * (n + 1) // 2
            if cost > min_cost:
                break
        min_cost = min(min_cost, cost)
    return min_cost


def get_data():
    return list(map(int, utils.get_lines(7)[0].split(',')))


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
