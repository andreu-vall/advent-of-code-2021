from collections import Counter
from pyperclip import copy
import utils


def part1(data):
    chain, elem = data
    for _ in range(10):
        new_chain = [chain[0]]
        for i in range(1, len(chain)):
            new_chain.append(elem[chain[i-1:i+1]])
            new_chain.append(chain[i])
        chain = ''.join(new_chain)
    count = Counter(chain)
    return max(count.values()) - min(count.values())


def part2(data):
    chain, elem = data
    count = Counter()
    for i in range(1, len(chain)):
        count[chain[i-1:i+1]] += 1
    for _ in range(40):
        new_count = Counter()
        for st, v in count.items():
            letter = elem[st]
            new_count[st[0]+letter] += v
            new_count[letter+st[1]] += v
        count = new_count
    let_count = Counter()
    for k, v in count.items():
        let_count[k[0]] += v
    let_count[chain[-1]] += 1
    return max(let_count.values()) - min(let_count.values())


def get_data():
    lines = utils.get_lines(14)
    start = lines[0]
    elem = {}
    for line in lines[2:]:
        k, v = line.split(' -> ')
        elem[k] = v
    return start, elem


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
