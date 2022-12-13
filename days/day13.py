from lib import load_input
from ast import literal_eval
import functools


def solve(data_in, part=1):
    data = [x.split("\n") for x in data_in.split("\n\n")]
    data2 = [literal_eval(x) for x in data_in.split("\n") if x]
    data2.extend([[[6]], [[2]]])
    return part_one(data) if part == 1 else part_two(data2)


def compare(left, right):
    r, l = 0, 0
    while True:
        try:
            elem1 = left[l]
            l += 1
        except IndexError:
            return None if len(left) == len(right) else True
        try:
            elem2 = right[r]
            r += 1
        except IndexError:
            return None if len(left) == len(right) else False
        if isinstance(elem1, list) and not isinstance(elem2, list):
            result = compare(elem1, [elem2])
            if result is None:
                continue
            return True if result else False
        elif isinstance(elem2, list) and not isinstance(elem1, list):
            result = compare([elem1], elem2)
            if result is None:
                continue
            return True if result else False
        elif isinstance(elem1, list) and isinstance(elem2, list):
            result = compare(elem1, elem2)
            if result is None:
                continue
            return True if result else False
        else:
            if elem1 == elem2:
                continue
            return True if elem1 < elem2 else False


def part_one(data):
    result = 0
    for i in range(len(data)):
        list1 = literal_eval(data[i][0])
        list2 = literal_eval(data[i][1])
        if compare(list1, list2):
            result += i + 1
    return result


def part_two(data):
    result = 1
    data.sort(key=functools.cmp_to_key(lambda item1, item2: -1 if compare(item1, item2) else 1))
    for i in range(len(data)):
        result *= (i + 1) if data[i] == [[2]] or data[i] == [[6]] else 1
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))