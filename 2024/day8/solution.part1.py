import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    pairs = {}
    rows = len(data)
    cols = len(data[0])
    antinode_map = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            a = data[i][j]
            if a != ".":
                if a not in pairs:
                    pairs[a] = []
                pairs[a].append((i, j))

    from itertools import combinations

    for a in pairs:
        for p1, p2 in combinations(pairs[a], 2):
            p3 = (2 * p1[0] - p2[0], 2 * p1[1] - p2[1])
            p4 = (2 * p2[0] - p1[0], 2 * p2[1] - p1[1])
            if p3[0] >= 0 and p3[0] < rows and p3[1] >= 0 and p3[1] < cols:
                antinode_map[p3[0]][p3[1]] = 1
            if p4[0] >= 0 and p4[0] < rows and p4[1] >= 0 and p4[1] < cols:
                antinode_map[p4[0]][p4[1]] = 1

    print(sum([sum(l) for l in antinode_map]))


if __name__ == "__main__":
    main()
