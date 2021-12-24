from pyperclip import copy
import numpy as np
import utils


def count_light(data, iterations):
    first, array = data
    infinite = 0
    for _ in range(iterations):
        nou_arr = np.empty((array.shape[0]+2, array.shape[1]+2), dtype=int)
        array = np.pad(array, pad_width=2, constant_values=infinite)
        for i in range(1, array.shape[0]-1):
            for j in range(1, array.shape[1]-1):
                mask = array[i-1:i+2, j-1:j+2].flatten()
                binary = ''.join(str(v) for v in mask)
                nou_arr[i-1][j-1] = first[int(binary, 2)]
        array = nou_arr
        infinite = first[int(str(infinite) * 9, 2)]
    return int(array.sum())


def part1(data):
    return count_light(data, 2)


def part2(data):
    return count_light(data, 50)


def get_data():
    lines = utils.get_lines(20)
    first = [int(ch == '#') for ch in lines[0]]
    array = np.array([[int(ch == '#') for ch in line] for line in lines[2:]])
    return first, array


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
