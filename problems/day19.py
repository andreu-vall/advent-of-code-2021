import multiprocessing as mp
import collections as col
import itertools as it
import numpy as np
import utils
import time


def get_data():
    lines = utils.get_lines(19)
    scanners = []
    for line in lines:
        if line == '':
            continue
        if line.startswith('---'):
            scanners.append([])
        else:
            scanners[-1].append(np.array(list(map(int, line.split(',')))))
    return scanners


# Generar el grup de les 24 matrius de rotacions de 90º en 3D
def rotations3d():
    x_rot = np.array([[1, 0, 0],    # x -> x'
                      [0, 0, 1],    # y -> y'
                      [0, -1, 0]])  # z -> z'

    y_rot = np.array([[0, 0, 1],
                      [0, 1, 0],
                      [-1, 0, 0]])

    """
    z_rot = np.array([[0, 1, 0],
                      [-1, 0, 0],
                      [0, 0, 1]])"""

    hashed, nous = {}, {arr.tobytes(): arr for arr in [x_rot, y_rot]}
    while nous:
        hashed.update(nous)
        nous = {}
        for arr1, arr2 in it.product(hashed.values(), repeat=2):
            prod = np.dot(arr1, arr2)
            assert np.linalg.det(prod) == 1
            hash_prod = prod.tobytes()
            if hash_prod not in hashed:
                nous[hash_prod] = prod

    return list(hashed.values())


def part1(data, rotations):
    # Crida a parallelized està paral·lelitzat, normal seria una única crida i ignorant part mòdulç
    cpus = min(mp.cpu_count(), len(data))
    a_pool = mp.Pool(cpus)
    result = a_pool.starmap(parallelized, [(data, i, rotations, cpus) for i in range(cpus)])

    relations = []
    for r in result:
        relations.extend(r)

    # Número beacon: [coordenada relativa respecte el Beacon 0, angle relatiu respecte el Beacon 0]
    positions = {0: [np.array([0, 0, 0]), np.identity(3, dtype=int)]}
    while len(positions) < len(data):
        for i, j, coord, rot in relations:
            if i in positions and j not in positions:
                primer, primer_rot = positions[i]
                second = primer + np.dot(primer_rot, coord)
                new_rot = np.dot(primer_rot, rot)  # No és commutatiu
                positions[j] = [second, new_rot]

    beacons = set()
    for k, (pos, rot) in positions.items():
        for row in data[k]:
            beacons.add(tuple(pos+np.dot(rot, row)))
    return len(beacons), positions


def parallelized(data, modulo, rotations, cpus):
    relations = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if j % cpus != modulo:
                continue
            coin, coord, rot = check(data[i], data[j], rotations)
            if coin:
                relations.append([i, j, coord, rot])
                inv = np.linalg.inv(rot).astype(int)
                relations.append([j, i, -np.dot(inv, coord), inv])
    return relations


def check(row1, row2, rotations):
    for rot in rotations:
        counter = col.Counter()
        perm = [np.dot(rot, row) for row in row2]
        for v1 in row1:
            for v2 in perm:
                counter[tuple(v1-v2)] += 1
        coord, times = counter.most_common(1)[0]
        if times >= 12:
            return True, coord, rot
    return False, 0, 0


def part2(positions):
    scanners = [v[0] for v in positions.values()]
    return max(np.abs(v1-v2).sum() for v1, v2 in it.product(scanners, repeat=2))


if __name__ == '__main__':
    start = time.perf_counter()
    rotations_ = rotations3d()
    answer1, positions_ = part1(get_data(), rotations_)
    print(answer1)              # 398
    print(part2(positions_))    # 10965
    print('it took', time.perf_counter()-start, 'seconds')
