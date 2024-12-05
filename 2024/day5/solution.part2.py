import os

import networkx as nx


def is_right_order(graph, update):
    n = len(update)
    for i in range(n):
        for j in range(i + 1, n):
            if graph.has_edge(update[j], update[i]):
                return False
    return True


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    g = nx.DiGraph()
    for i in range(10, 100):
        for j in range(10, 100):
            g.add_edge(i, j)

    updates = []
    for line in data:
        if line == "":
            continue
        elif "|" in line:
            p1, p2 = line.split("|")
            g.remove_edge(int(p2), int(p1))
        else:
            updates.append([int(num) for num in line.split(",")])

    ans = 0
    for update in updates:
        if not is_right_order(g, update):
            sub_graph = g.subgraph(update)
            update = sorted(update, key=lambda x: len(sub_graph.edges(x)), reverse=True)
            half = (len(update) - 1) / 2
            ans += update[int(half)]

    print(ans)


if __name__ == "__main__":
    main()
