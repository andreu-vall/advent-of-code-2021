from collections import defaultdict, Counter
from pyperclip import copy
import utils


def part1(data):
    return genera('start', {'start'}, False, data)


def genera(position, visited, doble, edges):
    if position == 'end':
        return 1
    count = 0
    for v in edges[position]:
        if v.islower():
            if v not in visited:
                visited.add(v)
                count += genera(v, visited, doble, edges)
                visited.remove(v)
            else:
                if doble and v != 'start':
                    count += genera(v, visited, False, edges)
        else:
            count += genera(v, visited, doble, edges)
    return count


def part2(data):
    return genera('start', {'start'}, True, data)


def get_data():
    edges = defaultdict(set)
    for u, v in [line.split('-') for line in utils.get_lines(12)]:
        edges[u].add(v)
        edges[v].add(u)
    return edges


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)

    """ Intent de juntar camins
    small_caves = {key for key in data if key.islower()}
    small_caves = {k: i for i, k in enumerate(small_caves)}

    start_tuple = [0] * len(small_caves)
    start_tuple[small_caves['start']] = 1
    start_tuple = tuple(start_tuple)

    vegades = Counter()
    start = 'start', start_tuple
    vegades[start] = 1

    pendent = [start]
    while pendent:
        vis,
        nou_pendent = []
        for p in pendent:


    return 0"""