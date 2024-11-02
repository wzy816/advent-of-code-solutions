import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    map = []
    for line in data:
        map.append(list(line))

    import networkx as nx

    start, end = (0, 1), (len(map) - 1, len(map[0]) - 2)

    # build grid graph
    g1 = nx.grid_2d_graph(len(map), len(map[0]))
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                g1.remove_node((i, j))

    # collapse 2-way node
    ns = [n for n in g1.nodes() if len(g1.edges(n)) == 2]
    for n in ns:
        e1, e2 = g1.edges(n)
        n1, n2 = g1.neighbors(n)
        w = g1.edges[e1].get("w", 1) + g1.edges[e2].get("w", 1)
        g1.add_edge(n1, n2, w=w)
        g1.remove_node(n)
    print(g1.edges(data=True))

    print(
        max([nx.path_weight(g1, p, "w") for p in nx.all_simple_paths(g1, start, end)])
    )
    # 6738


if __name__ == "__main__":
    main()
