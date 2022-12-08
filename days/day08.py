from lib import load_input
import numpy as np


def solve(data, part=1):
    data = np.array([list(map(int, list(x))) for x in data.splitlines()])
    return part_one(data) if part == 1 else part_two(data)


def part_one(data):
    l = len(data[0])
    invis = 0
    for i in range(1, l - 1):
        for j in range(1, l - 1):
            n = data[i][j]
            if not (all(data[i + 1:, j] < n) or all(data[:i, j] < n) or all(data[i, j + 1:] < n) or all(data[i, :j] < n)):
                invis += 1
    return l * l - invis


def part_two(data):
    l = len(data[0])
    max_score = 0
    for i in range(1, l - 1):
        for j in range(1, l - 1):
            n = data[i][j]
            score = 1
            bot = np.where(data[i + 1:, j] >= n)[0]
            top = np.where(data[:i, j][::-1] >= n)[0]
            right = np.where(data[i, j + 1:] >= n)[0]
            left = np.where(data[i, :j][::-1] >= n)[0]
            score *= bot[0] + 1 if len(bot) > 0 else l-i-1
            score *= top[0] + 1 if len(top) > 0 else i
            score *= right[0] + 1 if len(right) > 0 else l-j-1
            score *= left[0] + 1 if len(left) > 0 else j
            max_score = max(max_score, score)
    return max_score


if __name__ == "__main__":
    # print(solve(load_input("small")))
    print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
