import numpy as np
import utils


def last(data):
    moved, step = True, 0
    n, m = data.shape

    while moved:
        moved = False
        nou_data = np.copy(data)
        for i in range(n):
            for j in range(m):
                if data[i, j] == '>' and data[i, (j+1)%m] == '.':
                    moved = True
                    reverse(i, (j+1)%m, i, j, nou_data)

        data = nou_data
        nou_data = np.copy(data)

        for j in range(m):
            for i in range(n):
                if data[i, j] == 'v' and data[(i+1)%n, j] == '.':
                    moved = True
                    reverse((i+1)%n, j, i, j, nou_data)

        data = nou_data
        step += 1

    return step


def reverse(i1, j1, i2, j2, data):
    data[i1, j1], data[i2, j2] = data[i2, j2], data[i1, j1]


def part2(data):
    return 0


def get_data():
    return np.array([list(line) for line in utils.get_lines(25)])


if __name__ == '__main__':
    print(last(get_data()))
