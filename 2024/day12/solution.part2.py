import os
from itertools import combinations


def bfs(i, j, data, visited, id, region):

    visited[i][j] = 1

    if id not in region:
        region[id] = []
    region[id].append((i, j))

    label = data[i][j]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni > len(data) - 1 or nj < 0 or nj > len(data[0]) - 1:
            continue
        if visited[ni][nj] != 0:
            continue

        if data[ni][nj] == label:
            bfs(ni, nj, data, visited, id, region)


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])

    visited = [[0 for j in range(cols)] for i in range(rows)]
    region = {}  # id: [(i,j),(i2,j2),...]
    id = 1
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] != 0:
                continue
            bfs(i, j, data, visited, id, region)
            id += 1

    ans = 0

    for id, plots in region.items():
        area = len(plots)
        first_plot = plots[0]
        label = data[first_plot[0]][first_plot[1]]

        # build a side map
        # of shape (2*rows+1,2*cols+1)
        # id => plot location
        # x => a side on perimeter
        # empty string => no side here, or side not on perimeter

        # input:
        # AAAAAA
        # AAABBA
        # AAABBA
        # ABBAAA
        # ABBAAA
        # AAAAAA

        # side map for A(id=1)
        #   x   x   x   x   x   x
        # x 1   1   1   1   1   1 x
        #               x   x
        # x 1   1   1 x       x 1 x

        # x 1   1   1 x       x 1 x
        #       x   x   x   x
        # x 1 x       x 1   1   1 x

        # x 1 x       x 1   1   1 x
        #       x   x
        # x 1   1   1   1   1   1 x
        #   x   x   x   x   x   x

        side_map = [[" " for j in range(2 * cols + 1)] for i in range(2 * rows + 1)]

        sides = []

        for plot in plots:
            i, j = plot

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if (
                    (ni < 0 or ni > rows - 1)
                    or (nj < 0 or nj > cols - 1)
                    or (data[ni][nj] != label)
                ):
                    if ni == i:
                        if nj < j:
                            # left side
                            sides.append((2 * i + 1, 2 * j + 1 - 1))
                        else:
                            # right side
                            sides.append((2 * i + 1, 2 * j + 1 + 1))
                    elif nj == j:
                        if ni < i:
                            # up side
                            sides.append((2 * i + 1 - 1, 2 * j + 1))
                        else:
                            # down side
                            sides.append((2 * i + 1 + 1, 2 * j + 1))

        for s in sides:
            side_map[s[0]][s[1]] = "x"

        for plot in plots:
            i, j = plot
            side_map[2 * i + 1][2 * j + 1] = id

        # solution: number of sides = number of corners

        # 1. get all corners where diagnal x and x with/without id
        # x            x          1x          x          x         x1
        #  x    or    x     or    x     or   x1    or    1x    or   x

        # 2. for cases like
        # 1 x
        # x   x
        #   x 1
        #
        # or
        #   x 1
        # x   x
        # 1 x
        #
        # num of sides = 2, but 4 is counted, so find case and minus 2

        num_sides = 0

        for a, b in combinations(sides, 2):
            i1, j1 = a
            i2, j2 = b
            if abs(i1 - i2) == 1 and abs(j1 - j2) == 1:
                num_sides += 1

        for i in range(rows):
            for j in range(cols):
                ci = 2 * i
                cj = 2 * j
                if (
                    side_map[ci][cj - 1] == "x"
                    and side_map[ci][cj + 1] == "x"
                    and side_map[ci - 1][cj] == "x"
                    and side_map[ci + 1][cj] == "x"
                ):
                    if (
                        side_map[ci - 1][cj - 1] == id
                        and side_map[ci + 1][cj + 1] == id
                    ):
                        num_sides -= 2

                    if (
                        side_map[ci - 1][cj + 1] == id
                        and side_map[ci + 1][cj - 1] == id
                    ):
                        num_sides -= 2

        price = area * num_sides
        ans += price

    print(ans)


if __name__ == "__main__":
    main()
