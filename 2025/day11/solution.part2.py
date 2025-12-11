import math
import os
import time

import matplotlib.pyplot as plt
import networkx as nx


def count_paths(G, start, end):
    q = {start: 1}

    ans = 0
    while q:
        new_q = {}
        for node in q:
            cnt = q[node]
            for out_node in G.successors(node):
                if out_node in new_q:
                    new_q[out_node] += cnt
                else:
                    new_q[out_node] = cnt

        if end in new_q:
            ans += new_q[end]
        q = new_q.copy()

    return ans


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    g = nx.DiGraph()
    for row in data:
        start, ends = row.split(": ")
        for end in ends.split(" "):
            g.add_edge(start, end)

    # pos = pos = nx.spring_layout(g)
    # plt.figure(figsize=(10, 10))
    # nx.draw(g, pos=pos, node_size=2, width=1, arrowsize=4)
    # nx.draw_networkx_nodes(
    #     g, pos, nodelist=["dac", "fft"], node_color="red", node_size=2
    # )
    # nx.draw_networkx_labels(
    #     g,
    #     pos,
    #     labels={i: i for i in ["dac", "fft", "svr", "out"]},
    #     font_size=12,
    #     font_color="red",
    # )
    # plt.draw()
    # plt.savefig("./2025/day11/graph.png")

    ans1 = math.prod(
        [
            count_paths(g, source, target)
            for source, target in [
                ("svr", "fft"),
                ("fft", "dac"),
                ("dac", "out"),
            ]
        ]
    )
    ans2 = math.prod(
        [
            count_paths(g, source, target)
            for source, target in [
                ("svr", "dac"),
                ("dac", "fft"),
                ("fft", "out"),
            ]
        ]
    )
    print(ans1)
    print(ans2)


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main("input_demo2.txt")
    main("input.txt")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f} seconds")
