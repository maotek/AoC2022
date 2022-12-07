from lib import load_input


class Dir:
    def __init__(self, parent=None):
        self.parent = parent
        self.size = 0

    def add_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_size(size)


def make_dir(data):
    all_dirs = []
    cur = Dir()
    all_dirs.append(cur)
    for i in data:
        if "$ cd" in i:
            if ".." in i:
                cur = cur.parent
                continue
            cur = Dir(parent=cur)
            all_dirs.append(cur)
        elif "$ ls" not in i:
            file = i.split(" ")
            if file[0] != "dir":
                cur.add_size(int(file[0]))
    return all_dirs


def solve(data, part=1):
    data = data.splitlines()[1:]
    return part_one(data) if part == 1 else part_two(data)


def part_one(data):
    return sum(list(filter(lambda x: x < 100_000, [i.size for i in make_dir(data)])))


def part_two(data):
    all_dirs = make_dir(data)
    return min(list(filter(lambda x: x > all_dirs[0].size - 40_000_000, [i.size for i in all_dirs])))


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))