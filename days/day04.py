from lib import load_input


def solve(data, part=1):
    data = [[list(map(int, b.split("-"))) for b in a] for a in [x.split(",") for x in data.splitlines()]]
    return part_one(data) if part == 1 else part_two(data)


def part_one(data):
    return len(list(filter(lambda x: (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (x[1][0] <= x[0][0] and x[1][1] >= x[0][1]), data)))


def part_two(data):
    return len([z for z in [set(range(x[0][0], x[0][1]+1)).intersection(range(x[1][0], x[1][1]+1)) for x in data] if z])


if __name__ == "__main__":
    # print(solve(load_input("small")))
    print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
