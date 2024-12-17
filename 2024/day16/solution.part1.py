import os

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])

    start = None
    end = None

    G = nx.grid_2d_graph(rows, cols).to_directed()
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == "#":
                G.remove_node((i, j))
            if data[i][j] == "S":
                start = (i, j)
            if data[i][j] == "E":
                end = (i, j)

    for e in G.edges():
        start_node, end_node = e
        if start_node[0] == end_node[0]:
            if start_node[1] > end_node[1]:
                # e <- s
                G.edges[e]["pos"] = "W"
            else:
                # s -> e
                G.edges[e]["pos"] = "E"
        elif start_node[1] == end_node[1]:
            if start_node[0] > end_node[0]:
                # e
                # |
                # s
                G.edges[e]["pos"] = "N"
            else:
                # s
                # |
                # e
                G.edges[e]["pos"] = "S"

    print(G, start, end)
    while True:
        removed = 0
        for node in list(G.nodes()):
            if node == start or node == end:
                continue

            if len(list(G.neighbors(node))) == 1:
                G.remove_node(node)
                removed += 1
        if removed == 0:
            break

    print(G, start, end)

    for n in list(G.nodes()):
        G.nodes[n]["score"] = {
            "N": 1e20,
            "E": 1e20,
            "S": 1e20,
            "W": 1e20,
        }
    G.nodes[start]["score"]["W"] = 0
    G.nodes[start]["score"]["S"] = 0
    while True:
        updated = 0
        for start_node in list(G.nodes()):
            for end_node in G.neighbors(start_node):
                e = G.edges[start_node, end_node]
                start_node_score = G.nodes[start_node]["score"].copy()
                end_node_score = G.nodes[end_node]["score"]
                if e["pos"] == "N":
                    G.nodes[start_node]["score"]["N"] = min(
                        end_node_score["N"] + 1,
                        end_node_score["E"] + 1 + 1000,
                        end_node_score["W"] + 1 + 1000,
                    )
                if e["pos"] == "S":
                    G.nodes[start_node]["score"]["S"] = min(
                        end_node_score["S"] + 1,
                        end_node_score["E"] + 1 + 1000,
                        end_node_score["W"] + 1 + 1000,
                    )
                if e["pos"] == "E":
                    G.nodes[start_node]["score"]["E"] = min(
                        end_node_score["E"] + 1,
                        end_node_score["N"] + 1 + 1000,
                        end_node_score["S"] + 1 + 1000,
                    )
                if e["pos"] == "W":
                    G.nodes[start_node]["score"]["W"] = min(
                        end_node_score["W"] + 1,
                        end_node_score["N"] + 1 + 1000,
                        end_node_score["S"] + 1 + 1000,
                    )
                if start_node_score != G.nodes[start_node]["score"]:
                    updated += 1

        if updated == 0:
            break
    print(G.nodes[end]["score"])
    ans = min([v for k, v in G.nodes[end]["score"].items()])
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    # main("input_demo2.txt")
    main("input.txt")
