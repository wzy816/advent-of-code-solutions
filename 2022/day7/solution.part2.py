import os


class Directory:
    def __init__(self, name, parent_dir):
        self._name = name
        self._parent_dir = parent_dir
        self._children_dir = {}
        self._files = {}

    def add_file(self, file_name, file_size):
        self._files[file_name] = file_size

    def add_dir(self, child_dir):
        self._children_dir[child_dir.name] = child_dir

    def total_size(self):
        return sum(self._files.values()) + sum(
            [child.total_size() for child in self._children_dir.values()]
        )

    @property
    def name(self):
        return self._name

    @property
    def parent_dir(self):
        return self._parent_dir

    @property
    def children_dir(self):
        return self._children_dir


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    # tree traverse
    root = Directory("/", None)

    i = 0
    cur = root
    while i < len(data):
        line = data[i]
        if line.startswith("$ cd"):
            if line == "$ cd /":
                cur = root
            elif line == "$ cd ..":
                cur = cur.parent_dir
            else:
                child_dir_name = line.split(" ")[2]
                cur = cur.children_dir[child_dir_name]
            i += 1
        elif line == "$ ls":
            i += 1
            while i < len(data) and not data[i].startswith("$"):
                if data[i].startswith("dir"):
                    d = Directory(data[i].split(" ")[1], cur)
                    cur.add_dir(d)
                else:
                    file_size, file_name = data[i].split(" ")
                    cur.add_file(file_name, int(file_size))
                i += 1

    dir_sizes = []

    def dfs(c):
        dir_sizes.append(c.total_size())
        for child in c.children_dir.values():
            dfs(child)

    dfs(root)

    dir_sizes = sorted(dir_sizes)
    from bisect import bisect_left

    di = bisect_left(dir_sizes, 30000000 - (70000000 - root.total_size()))
    print(dir_sizes[di])

    # 8679207


if __name__ == "__main__":
    main()
