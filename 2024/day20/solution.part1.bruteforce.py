import os
from collections import Counter

import networkx as nx
from tqdm import tqdm


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    G = nx.grid_2d_graph(rows, cols)

    start, end = None, None
    walls = []
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == "#":
                G.remove_node((i, j))
                walls.append((i, j))
            if data[i][j] == "S":
                start = (i, j)
            if data[i][j] == "E":
                end = (i, j)

    dist = len(list(nx.shortest_path(G, start, end)))

    c = Counter()
    for wall in tqdm(walls):
        # add wall node
        i, j = wall
        G.add_node((i, j))

        # add wall edges
        for n2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if n2 in G.nodes():
                G.add_edge(n2, (i, j))

        dist2 = len(list(nx.shortest_path(G, start, end)))

        if dist - dist2 >= 100:
            c[dist - dist2] += 1

        # delet wall
        G.remove_node((i, j))

    print(sum([v for k, v in c.items()]))


if __name__ == "__main__":
    # main("input_demo.txt")

    main("input.txt")
