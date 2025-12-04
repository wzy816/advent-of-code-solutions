import os

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    g = nx.grid_2d_graph(rows, cols)

    # add diagnal edges
    for i in range(rows):
        for j in range(cols):
            for end in [
                (i - 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i + 1, j + 1),
            ]:
                if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
                    continue
                if ((i, j), end) not in g.edges:
                    g.add_edge((i, j), end)

    for i in range(rows):
        for j in range(cols):
            if data[i][j] == ".":
                g.remove_node((i, j))

    ans = 0

    while True:
        f = False
        nodes = list(g.nodes)
        for node in nodes:
            if len(g.edges(node)) < 4:
                g.remove_node(node)
                ans += 1
                f = True

        if not f:
            break

    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
