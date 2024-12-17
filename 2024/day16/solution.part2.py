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
                # ^
                # s
                G.edges[e]["pos"] = "N"
            else:
                # s
                # v
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
        }  # into node score
    G.nodes[start]["score"]["W"] = 0
    G.nodes[start]["score"]["S"] = 1000
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
    min_end_score = min([v for k, v in G.nodes[end]["score"].items()])
    best_end_directions = [
        k for k, v in G.nodes[end]["score"].items() if v == min_end_score
    ]
    print(min_end_score, best_end_directions)

    q = []
    for di in best_end_directions:
        q.append((end, di))

    for n in list(G.nodes()):
        G.nodes[n]["is_best"] = False

    while q:
        cur, cur_di = q.pop(0)
        cur_score = G.nodes[cur]["score"][cur_di]
        G.nodes[cur]["is_best"] = True

        for node2 in G.neighbors(cur):
            if G.nodes[node2]["is_best"]:
                continue

            e = G.edges[cur, node2]
            if e["pos"] != cur_di:
                continue

            node2_score = G.nodes[node2]["score"]

            if cur_di == "W":
                if node2_score["W"] + 1 == cur_score:
                    q.append((node2, "W"))
                if node2_score["N"] + 1 + 1000 == cur_score:
                    q.append((node2, "N"))
                if node2_score["S"] + 1 + 1000 == cur_score:
                    q.append((node2, "S"))
            elif cur_di == "E":
                if node2_score["E"] + 1 == cur_score:
                    q.append((node2, "E"))
                if node2_score["N"] + 1 + 1000 == cur_score:
                    q.append((node2, "N"))
                if node2_score["S"] + 1 + 1000 == cur_score:
                    q.append((node2, "S"))
            elif cur_di == "N":
                if node2_score["N"] + 1 == cur_score:
                    q.append((node2, "N"))
                if node2_score["E"] + 1 + 1000 == cur_score:
                    q.append((node2, "E"))
                if node2_score["W"] + 1 + 1000 == cur_score:
                    q.append((node2, "W"))
            elif cur_di == "S":
                if node2_score["S"] + 1 == cur_score:
                    q.append((node2, "S"))
                if node2_score["E"] + 1 + 1000 == cur_score:
                    q.append((node2, "E"))
                if node2_score["W"] + 1 + 1000 == cur_score:
                    q.append((node2, "W"))

    # display
    # for i in range(rows):
    #     for j in range(cols):
    #         if data[i][j] in "#SE":
    #             print(data[i][j], end="")
    #         elif data[i][j] == ".":
    #             if G.has_node((i, j)) and G.nodes[(i, j)]["is_best"]:
    #                 print("O", end="")
    #             else:
    #                 print(".", end="")
    #     print("\n", end="")

    print(sum([G.nodes[n]["is_best"] for n in list(G.nodes())]))


if __name__ == "__main__":
    # main("input_demo.txt")
    # main("input_demo2.txt")
    main("input.txt")
