with open("../inputs/day3.txt", "r") as f:
	data = [list(map(lambda x: ord(x)-96 if x.islower() else ord(x)-38,x)) for x in f.read().splitlines()]

def part_one(data):
	data = [set(y[:len(y)//2]).intersection(y[len(y)//2:]) for y in data]
	return sum([item for sublist in data for item in sublist])

def part_two(data):
	data = [set(x).intersection(y,z) for x,y,z in list(zip(*[iter(data)] * 3))]
	return sum([item for sublist in data for item in sublist])

print(part_one(data))
print(part_two(data))