import math
import os
from functools import cache
from itertools import product

import networkx as nx
from tqdm import tqdm


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    # +---+---+---+
    # | 7 | 8 | 9 |
    # +---+---+---+
    # | 4 | 5 | 6 |
    # +---+---+---+
    # | 1 | 2 | 3 |
    # +---+---+---+
    #     | 0 | A |
    #     +---+---+

    ng = nx.DiGraph()
    edges = [
        ("7", "8", ">"),
        ("7", "4", "v"),
        ("8", "7", "<"),
        ("8", "5", "v"),
        ("8", "9", ">"),
        ("9", "8", "<"),
        ("9", "6", "v"),
        ("4", "7", "^"),
        ("4", "5", ">"),
        ("4", "1", "v"),
        ("5", "8", "^"),
        ("5", "4", "<"),
        ("5", "6", ">"),
        ("5", "2", "v"),
        ("6", "9", "^"),
        ("6", "5", "<"),
        ("6", "3", "v"),
        ("1", "4", "^"),
        ("1", "2", ">"),
        ("2", "5", "^"),
        ("2", "1", "<"),
        ("2", "0", "v"),
        ("2", "3", ">"),
        ("3", "6", "^"),
        ("3", "2", "<"),
        ("3", "A", "v"),
        ("0", "2", "^"),
        ("0", "A", ">"),
        ("A", "3", "^"),
        ("A", "0", "<"),
    ]
    for n1, n2, d in edges:
        ng.add_edge(n1, n2, di=d)

    #     +---+---+
    #     | ^ | A |
    # +---+---+---+
    # | < | v | > |
    # +---+---+---+
    dg = nx.DiGraph()
    edges = [
        ("^", "A", ">"),
        ("^", "v", "v"),
        ("A", "^", "<"),
        ("A", ">", "v"),
        ("<", "v", ">"),
        ("v", "^", "^"),
        ("v", "<", "<"),
        ("v", ">", ">"),
        (">", "A", "^"),
        (">", "v", "<"),
    ]
    for n1, n2, d in edges:
        dg.add_edge(n1, n2, di=d)

    def run_pad(start, end, keypad):
        if start == end:
            return ["A"]
        ret = []
        for p in nx.all_shortest_paths(keypad, start, end):
            pg = nx.path_graph(p)
            dis = [keypad.edges[e]["di"] for e in pg.edges()]
            ret.append("".join(dis + ["A"]))
        return ret

    def run_once(seq, level):
        #  0-9A => ^V<>A num_keypad, level=2
        # ^V<>A => ^V<>A dir_keypad, level=1
        # ^V<>A => ^V<>A dir_keypad, level=0
        # ^V<>A => len()  no pad,    level=-1

        if level == -1:
            return len(seq)
        else:
            keypad = [dg, dg, ng][level]
            ans = 0
            for start, end in zip("A" + seq[:-1], seq):
                ans += min(
                    [run_once(seq2, level - 1) for seq2 in run_pad(start, end, keypad)]
                )
            return ans

    ans = 0
    for line in data:
        s = run_once(line, 2)
        ans += s * int(line[:-1])
    print(ans)


if __name__ == "__main__":
    main("input_demo.txt")
    # main("input.txt")
