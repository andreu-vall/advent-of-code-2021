import utils


pos = {'w': 0, 'x': 1, 'y': 2, 'z': 3}


def part1(data):
    return int(compute_alu([0, 0, 0, 0], data, 0, 0)[1])


def block(z, w, divide, sth1, sth2):
    x = (z % 26) + sth1 != w
    if divide:
        z //= 26
    if x:
        z = 26*z + w + sth2
    return z


def compute_alu(variables, data, i, depth):
    while True:
        if i == len(data) - 1:
            print('z is', variables[pos['z']])
            return variables[pos['z']] == 0, ''

        if data[i][0] == 'inp':
            for j in range(9, 0, -1):
                n_variables = variables[:]
                n_variables[pos[data[i][1]]] = j
                correct, numb = compute_alu(n_variables, data, i+1, depth+1)
                if correct:
                    return True, str(j) + numb
            return False, ''

        op = int(data[i][2]) if len(data[i][2]) > 1 or data[i][2].isnumeric() else variables[pos[data[i][2]]]

        match data[i][0]:
            case 'add':
                variables[pos[data[i][1]]] += op
            case 'mul':
                variables[pos[data[i][1]]] *= op
            case 'div':
                if op == 0:
                    print('Failed at depth', depth)
                    return False, ''
                variables[pos[data[i][1]]] //= op
            case 'mod':
                if variables[pos[data[i][1]]] < 0 or op <= 0:
                    print('Failed at depth', depth)
                    return False, ''
                variables[pos[data[i][1]]] %= op
            case 'eql':
                variables[pos[data[i][1]]] = int(op == variables[pos[data[i][1]]])
        i += 1


def part2(data):
    return 0


def get_data():
    return [line.split() for line in utils.get_lines(24)]


if __name__ == '__main__':
    print(part1(get_data()))
    print(part2(get_data()))
