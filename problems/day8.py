from pyperclip import copy
import utils


def part1(data):
    count = 0
    for _, op in data:
        for s in op:
            if len(s) in [2, 4, 3, 7]:
                count += 1
    return count


def part2(data):
    suma = 0
    for ip, op in data:
        for s in ip:
            if len(s) == 2:
                un = s
            if len(s) == 3:
                sett = s
            if len(s) == 4:
                quat = s

        digits = []
        for s in op:
            if len(s) == 2:
                dg = 1

            if len(s) == 3:
                dg = 7

            if len(s) == 4:
                dg = 4

            if len(s) == 5:
                if all(c in s for c in un):
                    dg = 3
                else:
                    if sum(c in s for c in quat) == 3:
                        dg = 5
                    else:
                        dg = 2

            if len(s) == 6:
                if not all(c in s for c in un):
                    dg = 6
                else:
                    if sum(c in s for c in quat) == 4:
                        dg = 9
                    else:
                        dg = 0

            if len(s) == 7:
                dg = 8

            digits.append(dg)

        suma += int(''.join(str(dg) for dg in digits))

    return suma


def get_data():
    data = []
    for line in utils.get_lines(8):
        ip, op = line.split(' | ')
        data.append((ip.split(), op.split()))
    return data


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
