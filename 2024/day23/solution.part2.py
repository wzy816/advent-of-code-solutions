import os

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    G = nx.Graph()
    G.add_edges_from([(line.split("-")[0], line.split("-")[1]) for line in data])

    ans = max(list(nx.find_cliques(G)), key=lambda c: len(c))
    print(",".join(sorted(ans)))


if __name__ == "__main__":
    # main("input_demo2.txt")
    main("input.txt")
