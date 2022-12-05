from lib import load_input
from collections import defaultdict
import re


def solve(data, part=1):
    data = [x.split("\n") for x in data.split("\n\n")]
    return part_one(data) if part == 1 else part_two(data)


def get_stacks(data):
    stacks = defaultdict(lambda: [])
    for j in range(len(data[0]) - 1):
        for i in range(1, len(data[0][j]), 4):
            if data[0][j][i] != ' ':
                stacks[((i - 1) // 4) + 1].append(data[0][j][i])
    for i in stacks.values():
        i.reverse()
    return stacks


def part_one(data):
    stacks = get_stacks(data)
    for j in data[1]:
        cut = list(map(int, re.findall("\d+", j)))
        for i in range(cut[0]):
            stacks[cut[2]].append(stacks[cut[1]].pop())
    return "".join([stacks[i + 1].pop() for i in range(len(stacks))])


def part_two(data):
    stacks = get_stacks(data)
    for j in data[1]:
        cut = list(map(int, re.findall("\d+", j)))
        stacks[cut[2]].extend(stacks[cut[1]][len(stacks[cut[1]]) - cut[0]:])
        stacks[cut[1]] = stacks[cut[1]][:len(stacks[cut[1]]) - cut[0]]
    return "".join([stacks[i+1].pop() for i in range(len(stacks))])


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
