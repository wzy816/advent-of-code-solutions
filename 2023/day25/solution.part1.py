import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    import networkx as nx

    g = nx.Graph()

    for line in data:
        node, neighbors = line.split(": ")
        neighbors = neighbors.split(" ")
        for neighbor in neighbors:
            g.add_edge(node, neighbor)

    for edge in nx.minimum_edge_cut(g):
        g.remove_edge(*edge)

    c1, c2 = nx.connected_components(g)
    print(len(c1) * len(c2))


if __name__ == "__main__":
    main()
