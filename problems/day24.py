import utils


def print_possibles(blocks):
    numb_divisions = sum(b[0] for b in blocks)
    max_z = 26 ** numb_divisions
    discarded = [set() for _ in range(len(blocks))]
    compute_alu(0, 0, blocks, max_z, discarded, '')


def compute_alu(z, depth, blocks, max_z, discarded, frag):
    """
    He aplicat bàsicament 2 optimitzacions:
    - Guardar 'caché' de (depth, z) dels valors impossibles per no repetir càlculs
    - Observant que la z >= 0 sempre i només es redueix amb les instruccions z //= 26, si comptem el (nombre
    d'instruccions z //= 26) = numb_divisions, sabem que la z < 26 ** numb_divisions, si no segur que al final no
    es podrà reduir prou per arribar a 0.
    Amb aquestes 2 optimitzacions es redueix de 9^14 a uns 5 segons.
    """
    if z >= max_z:
        return False

    if depth == len(blocks):
        if z == 0:
            print('Found:', int(frag))
        return z == 0

    if z in discarded[depth]:
        return False

    z_prev = z
    if blocks[depth][0]:
        max_z //= 26
    found_any = False
    for w in range(1, 10):
        z = block(z_prev, w, *blocks[depth])
        found_any = found_any or compute_alu(z, depth+1, blocks, max_z, discarded, frag + str(w))

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
    """
    Tots els blocs són de 18 línies i tenen exactament les mateixes instruccions, excepte la línia 5, 6 i 16.
    - En la 5 podem dividir z per 26 o per 1
    - En la  6 sumem un valor sth1 a x
    - En la 16 sumem un valor sth2 a y

    La variable w només s'utilitza per guardar inputs, i la x i la y per fer càlculs intermedis dins d'un bloc.
    Per tant les úniques variables rellevants de cada bloc ('input' del bloc) són la z i la w (input).
    L'output de cada bloc és la z
    """
    lines = utils.get_lines(24)
    blocks = []
    for i in range(len(lines)//18):
        divide = lines[18*i+4].split()[-1] == '26'
        sth1 = int(lines[18*i+5].split()[-1])
        sth2 = int(lines[18*i+15].split()[-1])
        blocks.append([divide, sth1, sth2])
    return blocks


if __name__ == '__main__':
    print_possibles(get_data())
