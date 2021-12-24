import utils


def get_data():
    result = []
    for line in utils.get_lines(22):
        cuboid = []
        action = line[:line.find(' ')]
        for _ in range(3):
            line = line[line.find('=')+1:]
            sep = line.find(',') if ',' in line else len(line)
            numb, line = line[:sep].split('..'), line[sep:]
            cuboid.append([int(numb[0]), int(numb[1])+1])
        result.append([action, cuboid])
    return result


def reactor_reboot(data):
    cuboids = []
    for action, cuboid in data:
        if action == 'on':
            nous = [cuboid]
            while nous:
                nou = nous.pop()
                for old in cuboids:
                    if has_intersection(old, nou):
                        nous.extend(cuboid_union(old, nou))
                        break
                else:
                    cuboids.append(nou)
        else:
            assert action == 'off'
            nou_cuboids = []
            for old in cuboids:
                if not has_intersection(old, cuboid):
                    nou_cuboids.append(old)
                else:
                    nou_cuboids.extend(cuboid_difference(old, cuboid))
            cuboids = nou_cuboids

        print(f'Numb of cuboids: {len(cuboids)}, Cuboid sum: {sum(volume(cub) for cub in cuboids)}')

    return sum(volume(cub) for cub in cuboids)


def has_intersection(cuboid1, cuboid2):
    for i in range(3):
        small, big = sorted([cuboid1[i], cuboid2[i]])
        if big[0] >= small[1]:
            return False
    return True


def get_copy(cuboid):
    return [cuboid[0][:], cuboid[1][:], cuboid[2][:]]


def cuboid_union(old, new):
    for i in range(3):
        for j in range(2):
            mul = 1 if j == 0 else -1
            if mul*new[i][j] < mul*old[i][j]:
                cop = get_copy(new)
                cop[i][1-j] = old[i][j]
                yield cop
                new[i][j] = old[i][j]


def cuboid_difference(old, new):
    return cuboid_union(new, old)


def volume(cuboid):
    vol = 1
    for i in range(3):
        vol *= cuboid[i][1] - cuboid[i][0]
    return vol


if __name__ == '__main__':
    print(reactor_reboot(get_data()))
