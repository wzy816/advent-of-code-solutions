import os

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows = 71
    cols = 71
    max_il = 1024

    g = nx.grid_2d_graph(rows, cols)
    for il, line in enumerate(data):
        y, x = map(int, line.split(","))
        g.remove_node((x, y))
        if il > max_il:
            break

    print(g)

    sp = nx.shortest_path(g, (0, 0), (rows - 1, cols - 1))
    print(sp)
    print(len(sp) - 1)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
