import itertools

with open("../inputs/day1.txt", "r") as f:
	data = f.read().splitlines()

def calories(data):
	return [sum(map(int, i)) for i in [list(x[1]) for x in itertools.groupby(data, lambda x: x == "") if not x[0]]]

def part_one(data):
	return max(calories(data))

def part_two(data):
	return sum(sorted(calories(data), reverse=True)[:3])

print(part_one(data))
print(part_two(data))