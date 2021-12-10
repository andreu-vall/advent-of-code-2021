from pyperclip import copy
import utils


def part1(data):
    suma = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            low = True
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= i+di < len(data) and 0 <= j+dj < len(data[i+di]):
                    if int(data[i+di][j+dj]) <= int(data[i][j]):
                        low = False
            if low:
                suma += 1 + int(data[i][j])

    return suma


def part2(data):
    basins = []
    pendent = {(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j]!='9'}
    while pendent:
        actual = pendent.pop()
        triats = {actual}
        buscar = {actual}
        while buscar:
            i, j = buscar.pop()
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= i+di < len(data) and 0 <= j+dj < len(data[i+di]):
                    if (i+di, j+dj) not in triats and data[i+di][j+dj] != '9':
                        triats.add((i+di, j+dj))
                        buscar.add((i+di, j+dj))
        pendent.difference_update(triats)
        basins.append(len(triats))
    basins.sort()
    x, y, z = basins[-3:]
    return x * y * z


def get_data():
    return utils.get_lines(9)


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
