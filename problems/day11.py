from pyperclip import copy
import numpy as np
import utils


def part1(data):
    count = 0
    for _ in range(100):
        data += 1
        flashed = set(zip(*np.where(data >= 10)))
        count += len(flashed)
        changed = list(flashed)
        while changed:
            i, j = changed.pop()
            for i2 in range(i-1, i+2):
                for j2 in range(j-1, j+2):
                    if 0 <= i2 < len(data) and 0 <= j2 < len(data[0]):
                        if (i2, j2) != (i, j) and (i2, j2) not in flashed:
                            data[i2, j2] += 1
                            if data[i2, j2] >= 10:
                                count += 1
                                flashed.add((i2, j2))
                                changed.append((i2, j2))

        data[np.where(data >= 10)] = 0

    return count


def part2(data):
    for step in range(1, 10000):
        data += 1
        flashed = set(zip(*np.where(data >= 10)))
        changed = list(flashed)
        while changed:
            i, j = changed.pop()
            for i2 in range(i-1, i+2):
                for j2 in range(j-1, j+2):
                    if 0 <= i2 < len(data) and 0 <= j2 < len(data[0]):
                        if (i2, j2) != (i, j) and (i2, j2) not in flashed:
                            data[i2, j2] += 1
                            if data[i2, j2] >= 10:
                                flashed.add((i2, j2))
                                changed.append((i2, j2))

        data[np.where(data >= 10)] = 0
        if len(flashed) == len(data[0]) * len(data):
            return step
    return 0


def get_data():
    return np.array([list(map(int, line)) for line in utils.get_lines(11)])


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
