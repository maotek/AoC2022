from lib import load_input


def solve(data, part=1):
    data = data.splitlines()
    return part_one(data) if part == 1 else part_two(data)


def part_one(data):
    pass


def part_two(data):
    pass


if __name__ == "__main__":
    print(solve(load_input("small")))
    # print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    # print(solve(load_input(), 2))
