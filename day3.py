from pyperclip import copy
import utils


def get_lines():
    return utils.get_input(3)


def base2(array):
    return int(''.join(str(dg) for dg in array), 2)


def part1(lines):
    count = [0] * len(lines[0])
    for line in lines:
        for i in range(len(line)):
            count[i] += line[i] == '1'

    half = len(lines) / 2
    numb1 = [int(val > half) for val in count]
    numb2 = [1 - val for val in numb1]

    return base2(numb1) * base2(numb2)


def part2(lines):
    values = []

    for politica in [lambda uns, zeros: uns>=zeros, lambda uns, zeros: uns<zeros]:

        possibles = lines[:]
        i = 0

        while len(possibles) > 1:
            uns = sum(p[i] == '1' for p in possibles)
            zeros = len(possibles) - uns
            buscat = str(int(politica(uns, zeros)))
            nou_possibles = []
            for p in possibles:
                if p[i] == buscat:
                    nou_possibles.append(p)
            i += 1
            possibles = nou_possibles

        values.append(int(possibles[0], 2))

    return values[0] * values[1]


if __name__ == '__main__':
    print(answer1 := part1(get_lines()))
    print(answer2 := part2(get_lines()))
    copy(answer2)
