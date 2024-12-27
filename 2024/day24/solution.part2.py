import math
import os
import random
import re
from collections import Counter, deque
from itertools import chain, combinations

import networkx as nx


def total_invalid_paths(graph):
    cnt = 0
    # xn->zn == XOR,XOR
    for i in range(1, 45):
        xn = f"x{i:02d}"
        zn = f"z{i:02d}"
        try:
            px = nx.shortest_path(graph, xn, zn)
            px_op = [graph.edges[e]["op"] for e in list(zip(px, px[1:]))]
            if px_op != ["XOR", "XOR"]:
                cnt += 1
        except:
            cnt += 1

    # xn->zn+1 == AND,OR,XOR
    for i in range(1, 44):
        xn = f"x{i:02d}"
        zn1 = f"z{i+1:02d}"
        try:
            px1 = nx.shortest_path(graph, xn, zn1)
            px1_op = [graph.edges[e]["op"] for e in list(zip(px1, px1[1:]))]
            if px1_op != ["AND", "OR", "XOR"]:
                cnt += 1
        except:
            cnt += 1
    return cnt


def build_graph(conns):
    g = nx.DiGraph()
    for g1, op, g2, g3 in conns:
        g.add_edge(g1, g3, op=op)
        g.add_edge(g2, g3, op=op)
    return g


def build_graph_with_swaps(conns, swaps):
    swap_dict = {}
    for s in swaps:
        swap_dict[s[0]] = s[1]
        swap_dict[s[1]] = s[0]

    g = nx.DiGraph()
    for g1, op, g2, g3 in conns:
        if g3 in swap_dict:
            g3 = swap_dict[g3]
        g.add_edge(g1, g3, op=op)
        g.add_edge(g2, g3, op=op)
    return g


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        ivs, conns = f.read().split("\n\n")

    #
    connections = []
    for conn in conns.split("\n"):
        g1, op, g2, g3 = re.findall(
            r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", conn
        )[0]
        connections.append([g1, op, g2, g3])

    swappable = [c[3] for c in connections]

    #
    d = deque([[]])

    while True:
        swaps = d.popleft()

        if swaps:
            g = build_graph_with_swaps(connections, swaps)
        else:
            g = build_graph(connections)

        #
        cur_cnt = total_invalid_paths(g)
        if cur_cnt == 0:
            print(",".join(sorted(list(chain(*swaps)))))
            return

        for n1, n2 in combinations(swappable, 2):
            if (n1, n2) in swaps or (n2, n1) in swaps:
                continue

            new_swaps = swaps + [(n1, n2)]
            g = build_graph_with_swaps(connections, new_swaps)

            if total_invalid_paths(g) < cur_cnt:
                d.append(new_swaps)
                break

    # visual solution
    print(",".join(sorted(["jqn", "cph", "kwb", "z12", "tgr", "z24", "qkf", "z16"])))


if __name__ == "__main__":
    main("input.txt")
