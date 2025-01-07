import os

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    G = nx.grid_2d_graph(rows, cols).to_directed()

    start, end, start_a = None, None, []
    for n in G.nodes():
        if data[n[0]][n[1]] == "S":
            start = n
            start_a.append(n)
        if data[n[0]][n[1]] == "E":
            end = n
        if data[n[0]][n[1]] == "a":
            start_a.append(n)

    for e in list(G.edges()):
        n1, n2 = e
        d1 = data[n1[0]][n1[1]]
        d2 = data[n2[0]][n2[1]]

        if d1 == "S":
            d1 = "a"
        if d1 == "E":
            d1 = "z"
        if d2 == "S":
            d2 = "a"
        if d2 == "E":
            d2 = "z"

        if ord(d2) - ord(d1) <= 1:
            continue
        else:
            G.remove_edge(n1, n2)

    # part 1
    print(len(nx.shortest_path(G, start, end)) - 1)

    # part2
    print(
        min(
            [
                len(nx.shortest_path(G, s, end)) - 1
                for s in start_a
                if nx.has_path(G, s, end)
            ]
        )
    )


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
