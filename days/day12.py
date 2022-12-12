from lib import load_input
from heapq import heappush, heappop
import sys


def solve(data, part=1):
    data = [[ord(y) - 96 for y in list(x)] for x in data.splitlines()]
    return part_one(data) if part == 1 else part_two(data)


def get_neighbours(x, y, max_x, max_y):
    return list(
        filter(lambda a: 0 <= a[0] < max_x and 0 <= a[1] < max_y, [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))


def ronaldo_stra(data, start, end):
    max_x = len(data[0])
    max_y = len(data)
    distances = dict()
    visited = set()
    backtrack = dict()
    pq = []
    s = start
    e = end
    for y in range(max_y):
        for x in range(max_x):
            distances[(y, x)] = sys.maxsize
            backtrack[(y, x)] = None
    distances[start] = 0
    heappush(pq, (0, *s))
    while len(pq) != 0:
        w, a, b = heappop(pq)
        visited.add((a, b))
        if (a, b) == e:
            break
        for y, x in get_neighbours(a, b, max_y, max_x):
            if (y, x) not in visited:
                if data[a][b] < data[y][x] <= data[a][b] + 1:
                    if distances[(y, x)] > w + 2:
                        heappush(pq, (w + 2, y, x))
                        distances[(y, x)] = w + 2
                        backtrack[(y, x)] = (a, b)
                if data[y][x] <= data[a][b]:
                    if distances[(y, x)] > w + 1:
                        heappush(pq, (w + 1, y, x))
                        distances[(y, x)] = w + 1
                        backtrack[(y, x)] = (a, b)
    root = e
    step = 0
    if backtrack[root] is None: # no path found
        return sys.maxsize
    while root != s:
        root = backtrack[root]
        step += 1
    return step


def part_one(data):
    max_x = len(data[0])
    max_y = len(data)
    start = None
    end = None
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == -13:
                start = (y, x)
                data[y][x] = 1
            if data[y][x] == -27:
                data[y][x] = 26
                end = (y, x)
    return ronaldo_stra(data, start, end)


def part_two(data):
    messi = sys.maxsize
    max_x = len(data[0])
    max_y = len(data)
    positions = []
    end = None
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == -13:
                data[y][x] = 1
            if data[y][x] == -13 or data[y][x] == 1:
                positions.append((y, x))
            if data[y][x] == -27:
                data[y][x] = 26
                end = (y, x)
    for start in positions:
        ronaldo = ronaldo_stra(data, start, end)
        if ronaldo < messi:
            messi = ronaldo
    return messi


if __name__ == "__main__":
    # print(solve(load_input("small")))
    print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))