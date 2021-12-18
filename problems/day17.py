from pyperclip import copy
import utils


"""
    pos, speed = 0, 0
    values, steps_possibles = [], {}
    while pos < x1:
        speed += 1
        pos += speed
        if x0 <= pos <= x1:
            values.append(pos)
            steps_possibles.update([speed])


def part1(data):
    x0, x1, y0, y1 = data
    print(data)
    count = 0
    best_value = float('-inf')
    for x_speed0 in range(x1):
        for y_speed0 in range(y0, 100):
            x, y = 0, 0
            x_speed, y_speed = x_speed0, y_speed0
            highest_y = y
            while x <= x1 and y >= y0:
                x += x_speed
                y += y_speed
                if x0 <= x <= x1 and y0 <= y <= y1:
                    count += 1
                    break
                highest_y = max(highest_y, y)
                x_speed = max(0, x_speed-1)
                y_speed -= 1
    return count
"""


def part1(data):
    x0, x1, y0, y1 = data
    count = 0
    for x_speed0 in range(x1+1):
        for y_speed0 in range(y0, 100):
            x, y = 0, 0
            x_speed, y_speed = x_speed0, y_speed0
            highest_y = y
            while x <= x1 and y >= y0:
                x += x_speed
                y += y_speed
                if x0 <= x <= x1 and y0 <= y <= y1:
                    count += 1
                    break
                highest_y = max(highest_y, y)
                x_speed = max(0, x_speed-1)
                y_speed -= 1
    return count


def part2(data):
    return 0


def get_data():
    line = utils.get_lines(17)[0]
    x_frag = line[line.find('=')+1:line.find(',')]
    x0, x1 = map(int, x_frag.split('..'))
    y_frag = line[line.rfind('=')+1:]
    y0, y1 = map(int, y_frag.split('..'))
    return x0, x1, y0, y1


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))  # 1873 too low
    copy(answer1)
