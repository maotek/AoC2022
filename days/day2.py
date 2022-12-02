with open("../inputs/day2.txt", "r") as f:
	data = [(ord(a)-64, ord(b)-87) for a,b in [x.split() for x in f.read().splitlines()]]

def part_one(data):
	sm = 0
	for i in data:
		# if(i[1] == (i[0] % 3) + 1):
		# 	sm += 6 + i[1]
		# elif(i[0] == i[1]):
		# 	sm += 3 + i[1]
		# else:
		# 	sm += i[1]
		sm += 6 + i[1] if (i[1] == (i[0] % 3) + 1) else (3 + i[1]) if (i[0] == i[1]) else i[1]
	return sm

def part_two(data):
	sm = 0
	for i in data:
		# if(i[1] == 3):
		# 	sm += 6 + (i[0] % 3) + 1
		# elif(i[1] == 2):
		# 	sm += 3 + i[0]
		# else:
		# 	sm += ((i[0] + 3 - 2) % 3) + 1
		sm += (6 + (i[0] % 3) + 1) if (i[1] == 3) else (3 + i[0]) if (i[1] == 2) else ((i[0] + 3 - 2) % 3) + 1
	return sm


print(part_one(data))
print(part_two(data))