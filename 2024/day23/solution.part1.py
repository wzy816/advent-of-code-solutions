import os

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    G = nx.Graph()
    for line in data:
        c1, c2 = line.split("-")
        G.add_edge(c1, c2)
    print(G)

    from itertools import combinations

    ans = {}
    for c in list(nx.find_cliques(G)):
        if len(c) >= 3:
            for subset in combinations(c, 3):
                if any([n.startswith("t") for n in subset]):
                    subset = tuple(sorted(subset))
                    if subset not in ans:
                        ans[subset] = 1

    print(len(ans.keys()))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
