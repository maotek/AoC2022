from lib import load_input


def solve(data, part=1):
    data = data.splitlines()[0]
    return part_one(data) if part == 1 else part_two(data)


def part_one(data):
    for i in range(len(data) - 3):
        if len(set(data[i:i + 4])) == 4:
            return i + 4


def part_two(data):
    for i in range(len(data) - 13):
        if len(set(data[i:i + 14])) == 14:
            return i + 14


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
