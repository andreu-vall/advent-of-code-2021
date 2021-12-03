from pyperclip import copy
import utils


def get_lines():
    return utils.split_lines(2)


def part1(lines):
    depth, hor_pos = 0, 0

    for direction, val in lines:
        if direction == 'forward':
            hor_pos += val
        elif direction == 'down':
            depth += val
        elif direction == 'up':
            depth -= val
        else:
            print('Yikes')

    return depth * hor_pos


def part2(lines):
    depth, hor_pos, aim = 0, 0, 0

    for direction, val in lines:
        if direction == 'forward':
            hor_pos += val
            depth += aim * val
        elif direction == 'down':
            aim += val
        elif direction == 'up':
            aim -= val
        else:
            print('Yikes')

    return depth * hor_pos


if __name__ == '__main__':
    print(answer1 := part1(get_lines()))
    print(answer2 := part2(get_lines()))
    copy(answer2)
