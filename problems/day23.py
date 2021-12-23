import heapq

hallway = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
room_start =   {11,   13,   15,   17}
room_end   =   {12,   14,   16,   18}

hallway_entry = {2,    4,    6,    8}
hallway_not_entry = hallway - hallway_entry
rooms = {11, 12, 13, 14, 15, 16, 17, 18}

get_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
get_room = {'A': {11, 12}, 'B': {13, 14}, 'C': {15, 16}, 'D': {17, 18}}

def neighbors(i):
    if 0 <= i <= 9:
        yield i + 1
    if 1 <= i <= 10:
        yield i - 1
    if i in hallway_entry:
        yield i + 9
    if i in room_start:
        yield i - 9
        yield i + 1
    if i in room_end:
        yield i - 1


def part1(data):
    heap = [(lower_bound(data), 0, data)]
    visited = {}
    end = tuple('...........AABBCCDD')
    while heap:
        bound, cost, pos = heapq.heappop(heap)
        if pos == end:
            return cost
        if pos not in visited:
            print(bound, cost, ''.join(pos))
            visited[pos] = cost
            for starts, cond in [(rooms, lambda s, e: e in hallway_not_entry),
                                 (hallway_not_entry, lambda s, e: e in get_room[pos[s]])]:
                for st in starts:
                    if pos[st] == '.':
                        continue
                    for ed, dist in get_reach_dist(st, pos).items():
                        if cond(st, ed):
                            nou = list(pos)
                            add_cost = dist * get_cost[nou[st]]
                            nou[st], nou[ed] = nou[ed], nou[st]
                            nou = tuple(nou)
                            if nou not in visited:
                                nou_cost = cost + add_cost
                                heapq.heappush(heap, (nou_cost + lower_bound(nou), nou_cost, nou))
    return 'Yikes'


def get_reach_dist(start, pos, ignore_others=False):
    distance, pending = {start: 0}, [(start, 0)]
    while pending:
        ac, dist = pending.pop()
        for vei in neighbors(ac):
            if not ignore_others and pos[vei] != '.':
                continue
            if vei not in distance:
                distance[vei] = dist + 1
                pending.append((vei, dist + 1))
    if not ignore_others:
        distance.pop(start)
    return distance


def lower_bound(pos):
    total_cost = 0
    for i, v in enumerate(pos):
        if v == '.':
            continue
        values = get_reach_dist(i, pos, True)
        total_cost += get_cost[v] * min(values[k] for k in get_room[v])
    return total_cost


def part2(data):
    return 0


if __name__ == '__main__':
    start_ = tuple('...........DBCADABC')
    # start_ = tuple('...........BACDBCDA')
    print(part1(start_))
    print(part2(start_))
