from pyperclip import copy
import heapq
import utils


def part1(data):
    heap = [(0, (0, 0))]
    visited = set()
    while heap:
        cost, pos = heapq.heappop(heap)
        if pos == (len(data)-1, len(data[-1])-1):
            return cost
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < len(data) and 0 <= nj < len(data[i]):
                heapq.heappush(heap, (cost+data[ni][nj], (ni, nj)))


def part2(data):
    nova_data = []
    for i in range(5):
        for line in data:
            nova_data.append([])
            for j in range(5):
                for v in line:
                    v += i+j
                    if v > 9:
                        v -= 9
                    nova_data[-1].append(v)
    return part1(nova_data)


def get_data():
    return [list(map(int, line)) for line in utils.get_lines(15)]


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
