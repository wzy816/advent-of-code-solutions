import os
import re
from itertools import permutations

import networkx as nx


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    G = nx.DiGraph()
    non_zero_valves = []
    for line in data:
        regex = r"Valve (\w+) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? ([\w\s,]+)"
        valve, rate, tunnels = re.findall(regex, line)[0]
        tunnels = tunnels.split(", ")
        rate = int(rate)
        if rate > 0:
            non_zero_valves.append(valve)

        G.add_node(valve, rate=rate)
        for tunnel in tunnels:
            G.add_edge(valve, tunnel)

    dist = {}
    for source, targets in list(nx.all_pairs_all_shortest_paths(G)):
        for target in targets:
            if target != source:
                dist[(source, target)] = min([len(p) for p in targets[target]])

    def dfs(node, time, visited, targets, score):
        if time <= 0:
            return score

        score += G.nodes[node]["rate"] * time

        visited.add(node)

        candidates = [
            dfs(n, time - dist[(node, n)], visited.copy(), targets, score)
            for n in targets
            if n not in visited
        ]

        return max(candidates + [score])

    # part1
    print(dfs("AA", 30, set(), non_zero_valves, 0))

    # part2
    def split_to_two(s):
        s = set(s)
        import itertools

        for r in range(1, len(s) // 2 + 1):
            for comb in itertools.combinations(s, r):
                yield set(comb), s - set(comb)

    print(
        max(
            [
                dfs("AA", 26, set(), me, 0) + dfs("AA", 26, set(), ele, 0)
                for me, ele in split_to_two(non_zero_valves)
            ]
        )
    )


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
