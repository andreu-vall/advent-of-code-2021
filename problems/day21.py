from pyperclip import copy
import numpy as np
import utils


def part1(data):
    pl1, pl2 = data
    return game1(pl1, pl2, 10, 100, 1000)


def game1(pl1, pl2, board_length, dice_length, score_win):
    positions = [pl1-1, pl2-1]
    scores = [0, 0]
    n_dice_rolled = 0
    while True:
        for i in range(2):
            dice_sum = 0
            for j in range(3):
                dice_sum += 1 + n_dice_rolled % dice_length
                n_dice_rolled += 1

            positions[i] = (positions[i] + dice_sum) % board_length
            scores[i] += 1 + positions[i]

            if scores[i] >= score_win:
                return scores[1-i] * n_dice_rolled


def part2(data):
    pl1, pl2 = data
    cache = {}
    res = game2((pl1-1, pl2-1), (0, 0), cache, 0)
    return int(max(res))


def game2(pos, scores, cache, turn):
    if (pos, scores, turn) in cache:
        return cache[(pos, scores, turn)]

    if scores[1-turn] >= 21:
        res = np.array([0, 0], dtype='int64')
        res[1-turn] = 1
        return res

    value = np.array([0, 0], dtype='int64')

    for dice in possibles:
        n_pos = list(pos)
        n_pos[turn] = (n_pos[turn] + dice) % 10
        n_pos = tuple(n_pos)

        n_scores = list(scores)
        n_scores[turn] += 1 + n_pos[turn]
        n_scores = tuple(n_scores)

        n_value = game2(n_pos, n_scores, cache, 1-turn)

        value += n_value

    cache[(pos, scores, turn)] = value

    return value


def get_possibles(x=3):
    if x == 1:
        return [1, 2, 3]
    ant = get_possibles(x-1)
    res = []
    for i in [1, 2, 3]:
        for a in ant:
            res.append(a+i)
    return res


def get_data():
    lines = utils.get_lines(21)
    pl1 = int(lines[0].split()[-1])
    pl2 = int(lines[1].split()[-1])
    return pl1, pl2


if __name__ == '__main__':
    possibles = get_possibles()
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
