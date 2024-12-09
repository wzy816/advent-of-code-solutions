import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    pairs = {}
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            a = data[i][j]
            if a != ".":
                if a not in pairs:
                    pairs[a] = []
                pairs[a].append((i, j))

    from itertools import combinations

    antinode_map = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if data[i][j] != ".":
                antinode_map[i][j] = 1
    for a in pairs:
        for p1, p2 in combinations(pairs[a], 2):
            i = 1
            while True:
                x1 = p1[0] + i * (p1[0] - p2[0])
                y1 = p1[1] + i * (p1[1] - p2[1])
                if x1 < 0 or x1 >= rows or y1 < 0 or y1 >= cols:
                    break
                antinode_map[x1][y1] = 1
                i += 1

            i = 1
            while True:
                x1 = p2[0] + i * (p2[0] - p1[0])
                y1 = p2[1] + i * (p2[1] - p1[1])
                if x1 < 0 or x1 >= rows or y1 < 0 or y1 >= cols:
                    break
                antinode_map[x1][y1] = 1
                i += 1

    print(sum([sum(l) for l in antinode_map]))


if __name__ == "__main__":
    main()
