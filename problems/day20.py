from pyperclip import copy
import numpy as np
import utils


def count_light(data, iterations):
    first, array = data
    infinite = '.'
    for _ in range(iterations):
        array = np.pad(array, pad_width=2, constant_values=infinite)
        # Maybe utilitzant moving windows amb funció custom és molt més ràpid
        nou_arr = []
        for i in range(1, array.shape[0]-1):
            nou_arr.append([])
            for j in range(1, array.shape[1]-1):
                mask = array[i-1:i+2, j-1:j+2].flatten()
                binary = ''.join(mask).replace('.', '0').replace('#', '1')
                nou_arr[-1].append(first[int(binary, 2)])
        array = np.array(nou_arr)
        infinite_binary = (infinite*9).replace('.', '0').replace('#', '1')
        infinite = first[int(infinite_binary, 2)]
    return int((array == '#').sum())


def part1(data):
    return count_light(data, 2)


def part2(data):
    return count_light(data, 50)


def get_data():
    lines = utils.get_lines(20)
    first = lines[0]
    array = np.array([list(line) for line in lines[2:]])
    return first, array


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
