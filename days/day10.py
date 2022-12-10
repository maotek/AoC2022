from lib import load_input


def solve(data, part=1):
    data = data.splitlines()
    return part_one(data) if part == 1 else part_two(data)


def part_one(data):
    cycle = 1
    x = 1
    result = 0
    for i in data:
        if i.startswith("addx"):
            for _ in range(2):
                if cycle in [20, 60, 100, 140, 180, 220]:
                    result += cycle * x
                cycle += 1
            x += int(i.split(" ")[1])
        else:
            if cycle in [20, 60, 100, 140, 180, 220]:
                result += cycle * x
            cycle += 1
    return result


def part_two(data):
    crt = [["." for i in range(40)] for j in range(6)]
    cycle = 0
    sprite = 1
    for i in data:
        if i.startswith("addx"):
            for _ in range(2):
                if sprite - 1 <= cycle % 40 <= sprite + 1:
                    crt[cycle // 40][cycle % 40] = "#"
                cycle += 1
            sprite += int(i.split(" ")[1])
        else:
            if sprite - 1 <= cycle % 40 <= sprite + 1:
                crt[cycle // 40][cycle % 40] = "#"
            cycle += 1
    for i in crt:
        print("".join(i))


if __name__ == "__main__":
    # print(solve(load_input("small")))
    print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
