from pyperclip import copy
import numpy as np
import utils


def part1(grid, folds):
    folds = [folds[0]]
    return part2(grid, folds)


def part2(grid, folds):
    for ax, numb in folds:
        if ax == 'y':
            half = grid.shape[0]//2
            assert half == numb
            grid = grid[:half, :] + np.flipud(grid[half+1:, :])

        if ax == 'x':
            half = grid.shape[1]//2
            assert half == numb
            grid = grid[:, :half] | np.fliplr(grid[:, half+1:])

    for arr in grid:
        st = ""
        for v in arr:
            st += '#' if v else ' '
        print(st)
    return int(grid.sum())


def get_data():
    points, folds, first_part = [], [], True
    for line in utils.get_lines(13):
        if first_part:
            if not line:
                first_part = False
            else:
                points.append(list(map(int, line.split(','))))
        else:
            line = line.split()[2]
            ax, numb = line.split('=')
            folds.append([ax, int(numb)])

    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    grid = np.zeros((max_y+1, max_x+1), dtype=bool)
    for x, y in points:
        grid[y][x] = 1
    return grid, folds


if __name__ == '__main__':
    print(answer1 := part1(*get_data()))
    print(answer2 := part2(*get_data()))
    copy(answer1)
