import collections
import itertools
import heapq

hallway = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
hallway_entry = {2,    4,    6,    8}
room_start   = {11,   12,   13,   14}

hallway_not_entry = hallway - hallway_entry

get_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def neighbors(i, room_length):
    if i in hallway:
        if i + 1 in hallway:
            yield i + 1
        if i - 1 in hallway:
            yield i - 1
        if i in hallway_entry:
            yield 10 + i//2
    else:
        if i in room_start:
            yield (i-10) * 2
        if i >= 15:
            yield i - 4
        room_end = 11 + 4 * (room_length-1)
        if i < room_end:
            yield i + 4


def game(start):
    room_length = len(start) // 4
    start = tuple('.' * len(hallway) + start)
    end = tuple('.' * len(hallway) + 'ABCD' * room_length)
    rooms = list(range(11, 11 + 4*room_length))
    get_room = {'ABCD'[i]: list(range(11+i, 11+4*room_length, 4)) for i in range(4)}
    heap = [(lower_bound(start, room_length, get_room), 0, start)]
    visited = {}
    while heap:
        bound, cost, pos = heapq.heappop(heap)
        if pos == end:
            return cost
        if pos not in visited:
            visited[pos] = cost
            for starts, cond in [(rooms, lambda s, e: e in hallway_not_entry),
                                 (hallway_not_entry, lambda s, e: e in get_room[pos[s]] and
                                                                  all(pos[v]=='.' or pos[v]==pos[s] for v in get_room[pos[s]]))]:
                for st in starts:
                    if pos[st] == '.':
                        continue
                    for ed, dist in get_reach_dist(st, pos, room_length).items():
                        if cond(st, ed):
                            nou = list(pos)
                            add_cost = dist * get_cost[nou[st]]
                            nou[st], nou[ed] = nou[ed], nou[st]
                            nou = tuple(nou)
                            if nou not in visited:
                                nou_cost = cost + add_cost
                                heapq.heappush(heap, (nou_cost + lower_bound(nou, room_length, get_room), nou_cost, nou))
    return 'Yikes'


def get_reach_dist(start, pos, room_length, ignore_others=False):
    distance, pending = {start: 0}, [(start, 0)]
    while pending:
        ac, dist = pending.pop()
        for vei in neighbors(ac, room_length):
            if not ignore_others and pos[vei] != '.':
                continue
            if vei not in distance:
                distance[vei] = dist + 1
                pending.append((vei, dist + 1))
    if not ignore_others:
        distance.pop(start)
    return distance


def lower_bound(pos, room_length, get_room):
    total_cost = 0
    dic = collections.defaultdict(list)
    for i, v in enumerate(pos):
        if v != '.':
            dic[v].append(i)
    for k in dic:
        values = []
        for i in dic[k]:
            val = get_reach_dist(i, pos, room_length, True)
            values.append([val[j] for j in get_room[k]])
        mi = float('inf')
        for comb in itertools.permutations(range(room_length)):
            cos = 0
            for j in range(room_length):
                cos += values[j][comb[j]]
            mi = min(mi, cos)
        total_cost += get_cost[k] * mi
    return total_cost


if __name__ == '__main__':

    print(game('DCDB'
               'BAAC'))

    print(game('DCDB'
               'DCBA'
               'DBAC'
               'BAAC'))
