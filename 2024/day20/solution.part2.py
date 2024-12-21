import os
from collections import Counter
from itertools import combinations

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    g = nx.grid_2d_graph(rows, cols)

    start = None
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == "#":
                g.remove_node((i, j))
            if data[i][j] == "S":
                start = (i, j)

    dist = nx.single_source_dijkstra_path_length(g, start)

    cheat = Counter()
    for ((x1, y1), d1), ((x2, y2), d2) in combinations(dist.items(), 2):
        d = abs(x1 - x2) + abs(y1 - y2)
        if d <= 20 and d2 - d1 - d >= 100:
            cheat[d2 - d1] += 1

    print(sum([v for k, v in cheat.items()]))


if __name__ == "__main__":
    # main("input_demo.txt")

    main("input.txt")
