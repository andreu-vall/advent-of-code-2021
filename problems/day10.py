from pyperclip import copy
import utils


def part1(data):
    claus = ['([{<', ')]}>', [3, 57, 1197, 25137]]
    suma = 0
    for line in data:
        stack = []
        for c in line:
            if c in claus[1]:
                val = claus[1].index(c)
                if val != stack[-1]:
                    suma += claus[2][val]
                    break
                stack.pop()
            else:
                stack.append(claus[0].index(c))
    return suma


def part2(data):
    claus = ['([{<', ')]}>', [1, 2, 3, 4]]
    scores = []
    for line in data:
        skip = False
        stack = []
        for c in line:
            if c in claus[1]:
                val = claus[1].index(c)
                if val != stack[-1]:
                    skip = True
                    break
                stack.pop()
            else:
                stack.append(claus[0].index(c))

        if not skip:
            score = 0
            for c in stack[::-1]:
                score = 5*score + claus[2][c]
            scores.append(score)

    return sorted(scores)[len(scores)//2]


def get_data():
    return utils.get_lines(10)


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
