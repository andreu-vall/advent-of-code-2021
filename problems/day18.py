from pyperclip import copy
import utils
from copy import deepcopy


def part1(data):
    val = data[0]
    for right in data[1:]:
        val = [val, right]
        while reduce(val):
            pass
    return magnitude(val)


def magnitude(pair):
    if isinstance(pair, int):
        return pair
    return 3*magnitude(pair[0]) + 2*magnitude(pair[1])


def reduce(pair):
    if explode(pair, []):
        return True
    return split(pair, [])


def explode(pair, index):
    if isinstance(access(pair, index), int):
        return False

    if len(index) < 4:
        return explode(pair, index+[0]) or explode(pair, index+[1])

    left, right = access(pair, index)

    left_index = find_left(pair, index)
    if left_index is not None:
        edit(pair, left_index, access(pair, left_index)+left)

    right_index = find_right(pair, index)
    if right_index is not None:
        edit(pair, right_index, access(pair, right_index)+right)

    edit(pair, index, 0)

    return True


def split(pair, index):
    val = access(pair, index)

    if isinstance(val, list):
        return split(pair, index+[0]) or split(pair, index+[1])

    if val <= 9:
        return False

    left = val // 2
    edit(pair, index, [left, val-left])
    return True


def access(pair, index_list):
    val = pair
    for idx in index_list:
        val = val[idx]
    return val


def edit(pair, index_list, new_val):
    val = pair
    for idx in index_list[:-1]:
        val = val[idx]
    val[index_list[-1]] = new_val


def find_left(pair, index_list):
    idx = rfind(index_list, 1)
    if idx != -1:
        left_index = index_list[:idx] + [0]
        while isinstance(access(pair, left_index), list):
            left_index += [1]
        return left_index
    return None


def find_right(pair, index_list):
    idx = rfind(index_list, 0)
    if idx != -1:
        right_index = index_list[:idx] + [1]
        while isinstance(access(pair, right_index), list):
            right_index += [0]
        return right_index
    return None


def rfind(lst, val):
    for idx, v in enumerate(reversed(lst)):
        if v == val:
            return len(lst) - 1 - idx
    return -1


def part2(data):
    best = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                mag = part1([deepcopy(data[i]), deepcopy(data[j])])
                best = max(best, mag)
    return best


def get_data():
    return [eval(line) for line in utils.get_lines(18)]


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
