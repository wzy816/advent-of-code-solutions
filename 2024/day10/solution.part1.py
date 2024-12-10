import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    map = []
    paths = []
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(int(data[i][j]))

            if data[i][j] == "0":
                paths.append([(i, j, 0)])
        map.append(r)

    for num in range(1, 10):
        new_paths = []
        for p in paths:
            last_i, last_j, last_n = p[-1]
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i = last_i + di
                j = last_j + dj
                if i < 0 or i >= rows or j < 0 or j >= cols:
                    continue
                if map[i][j] == num:
                    new_paths.append(p + [(i, j, num)])
        paths = new_paths

    ans = len(set([(p[0], p[-1]) for p in paths]))
    print(ans)


if __name__ == "__main__":
    main()
