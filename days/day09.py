from lib import load_input
from operator import add, sub


def solve(data, part=1):
    data = [x.split(" ") for x in data.splitlines()]
    return part_one(data) if part == 1 else part_two(data)


def in_range(h_x, h_y, t_x, t_y) -> bool:
    return h_x - 1 <= t_x <= h_x + 1 and h_y - 1 <= t_y <= h_y + 1


def part_one(data):
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
    visited = set()
    for direction, amount in data:
        for _ in range(int(amount)):
            prev_x, prev_y = head_x, head_y
            head_x += 1 if direction == "R" else -1 if direction == "L" else 0
            head_y += 1 if direction == "U" else -1 if direction == "D" else 0
            if not in_range(head_x, head_y, tail_x, tail_y):
                tail_x, tail_y = prev_x, prev_y
                visited.add((tail_x, tail_y))
    return len(visited) + 1


def part_two(data):
    head_x, head_y = 0, 0
    ropes = [[0, 0] for i in range(9)]
    visited = set()
    for direction, amount in data:
        for _ in range(int(amount)):
            prev_x, prev_y = head_x, head_y
            head_x += 1 if direction == "R" else -1 if direction == "L" else 0
            head_y += 1 if direction == "U" else -1 if direction == "D" else 0
            cur_x, cur_y = head_x, head_y
            move = None
            for rope in range(len(ropes)):
                next_x, next_y = ropes[rope]
                if not in_range(cur_x, cur_y, next_x, next_y):
                    c = list(map(sub, [cur_x, cur_y], [next_x, next_y]))
                    if c[0] == 0 or c[1] == 0:
                        # reset prev
                        if move is not None:
                            move = None
                            prev_x, prev_y = next_x + int(c[0] / 2), next_y + int(c[1] / 2)
                            
                    m = list(map(sub, [prev_x, prev_y], [next_x, next_y]))
                    if m[0] != 0 and m[1] != 0 and move is None:
                        move = m

                    if move is not None:
                        ropes[rope] = list(map(add, ropes[rope], move))
                        prev_x, prev_y = ropes[rope]  # adjust
                        cur_x, cur_y = prev_x, prev_y
                        prev_x, prev_y = next_x, next_y
                        if rope == 8:
                            visited.add((ropes[rope][0], ropes[rope][1]))
                    else:
                        ropes[rope] = [prev_x, prev_y]
                        cur_x, cur_y = prev_x, prev_y
                        prev_x, prev_y = next_x, next_y
                        if rope == 8:
                            visited.add((ropes[rope][0], ropes[rope][1]))
                else:
                    break
    return len(visited) + 1


if __name__ == "__main__":
    # print(solve(load_input("small")))
    print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))