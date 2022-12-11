from lib import load_input
import re
from math import floor
from operator import mul


def solve(data, part=1):
    data = data.split("\n\n")
    return part_one(data) if part == 1 else part_two(data)


class Monkey:
    def __init__(self, items, operator, operand, false, true, div, lcm):
        self.items = items
        self.operator = operator
        self.operand = operand
        self.to_false = false
        self.to_true = true
        self.div = div
        self.lcm = lcm
        self.inspections = 0

    def inspect(self):
        out = []
        for i in self.items:
            self.inspections += 1
            operand = i if self.operand == "old" else int(self.operand)
            new = floor((i * operand) // 3) if self.operator == "*" else floor((i + operand) // 3)
            to = self.to_true if new % self.div == 0 else self.to_false
            out.append((to, new))
        self.items.clear()
        return out

    def inspect_2(self):
        out = []
        for i in self.items:
            self.inspections += 1
            operand = i if self.operand == "old" else int(self.operand)
            new = i * operand if self.operator == "*" else i + operand
            to = self.to_true if new % self.div == 0 else self.to_false
            out.append((to, new % self.lcm))
        self.items.clear()
        return out


def parse(data):
    monkeys = []
    lcm = 1
    for j in data:
        lcm *= int(re.findall("\d+", j.split("\n")[3])[0])
    for i in data:
        monkey = i.split("\n")
        items = list(map(int, list(monkey[1].split(": ")[1].split(", "))))
        div = int(re.findall("\d+", monkey[3])[0])
        to_true = int(re.findall("\d+", monkey[4])[0])
        to_false = int(re.findall("\d+", monkey[5])[0])
        operation = monkey[2].split("= old")[1]
        operator = re.findall(r'[+*]', operation)[0]
        operand = monkey[2].split(operator + " ")[1]
        mnk = Monkey(items, operator, operand, to_false, to_true, div, lcm)
        monkeys.append(mnk)
    return monkeys


def part_one(data):
    monkeys = parse(data)
    for i in range(20):
        for monkey in monkeys:
            throws = monkey.inspect()
            for j in throws:
                monkeys[j[0]].items.append(j[1])
    sort = sorted([i.inspections for i in monkeys], reverse=True)
    return sort[0] * sort[1]


def part_two(data):
    monkeys = parse(data)
    for i in range(10000):
        for monkey in monkeys:
            throws = monkey.inspect_2()
            for j in throws:
                monkeys[j[0]].items.append(j[1])
    sort = sorted([i.inspections for i in monkeys], reverse=True)
    return sort[0] * sort[1]


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
