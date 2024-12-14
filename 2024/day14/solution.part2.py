import os
import re

import numpy as np


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    wide = 101
    tall = 103
    half_wide = wide // 2

    robots = []
    for line in data:
        p, v = line.split(" ")
        px, py = map(int, re.findall(r"p=(\d+),(\d+)", p)[0])
        vx, vy = map(int, re.findall(r"v=(-?\d+),(-?\d+)", v)[0])
        robots.append([px, py, vx, vy])

    step = 0
    while True:
        step += 1

        m = [[0] * wide for _ in range(tall)]
        for r in robots:
            r[0] = (r[0] + r[2]) % wide
            r[1] = (r[1] + r[3]) % tall

            m[r[1]][r[0]] = 1

        # solution:
        # check if majority robots is bottom triangular area (marked with 1)
        # [[0 0 0 0 0 0 0 0 0 0 0]
        #  [0 0 0 0 0 1 0 0 0 0 0]
        #  [0 0 0 0 1 1 1 0 0 0 0]
        #  [0 0 0 1 1 1 1 1 0 0 0]
        #  [0 0 0 1 1 1 1 1 0 0 0]
        #  [0 0 1 1 1 1 1 1 1 0 0]
        #  [0 1 1 1 1 1 1 1 1 1 0]]

        arr = np.array(m)
        total = np.sum(arr)

        i, j = np.indices(arr.shape)
        t1 = np.ceil((i / tall + j / half_wide) < 1).astype(bool)
        t2 = np.ceil(i / tall <= (j / half_wide - 1)).astype(bool)
        arr[t2 | t1] = 0
        tree_total = np.sum(arr)

        if tree_total / total > 0.8:
            for a in m:
                print("".join(["#" if x else "." for x in a]))
            print(step, tree_total / total)
            break


if __name__ == "__main__":
    main()
