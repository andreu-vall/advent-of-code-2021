import utils


def find_possibles(blocks):
    numb_divisions = sum(b[0] for b in blocks)
    max_z = 26 ** numb_divisions
    discarded = [set() for _ in range(len(blocks))]
    possibles = []
    compute_alu(0, 0, blocks, max_z, discarded, '', possibles)
    return possibles


def compute_alu(z, depth, blocks, max_z, discarded, frag, possibles):
    if z >= max_z:
        return False

    if depth == len(blocks):
        if z == 0:
            print('Found:', int(frag))
            possibles.append(int(frag))
        return z == 0

    if z in discarded[depth]:
        return False

    z_prev = z
    if blocks[depth][0]:
        max_z //= 26
    found_any = False
    for w in range(1, 10):
        z = block(z_prev, w, *blocks[depth])
        found_any = found_any or compute_alu(z, depth+1, blocks, max_z, discarded, frag + str(w), possibles)

    if not found_any:
        discarded[depth].add(z_prev)


def block(z, w, divide, sth1, sth2):
    x = (z % 26) + sth1 != w
    if divide:
        z //= 26
    if x:
        z = 26*z + w + sth2
    return z


def get_data():
    lines = utils.get_lines(24)
    blocks = []
    for i in range(len(lines)//18):
        divide = lines[18*i+4].split()[-1] == '26'
        sth1 = int(lines[18*i+5].split()[-1])
        sth2 = int(lines[18*i+15].split()[-1])
        blocks.append([divide, sth1, sth2])
    return blocks


if __name__ == '__main__':
    possibles_ = find_possibles(get_data())
    print(max(possibles_))
    print(min(possibles_))
