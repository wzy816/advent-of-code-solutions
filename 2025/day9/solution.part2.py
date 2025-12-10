import os
import time
from itertools import combinations, product

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import seaborn as sns


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    # get points
    points = []
    for d in data:
        x, y = map(int, d.split(","))
        points.append((x, y))

    # find anomaly points
    radius = 50000
    p_upper = None
    p_lower = None
    for p in points:
        if (p[0] - radius) ** 2 + (p[1] - radius) ** 2 < (0.9 * radius) ** 2:
            if p[1] > radius:
                p_upper = p
            else:
                p_lower = p

    # search for pair in upper/lower semisphere
    ans = 0
    ans_rect = None

    combo1 = product([p_upper], [p for p in points if p[1] > p_upper[1]])
    combo2 = product([p_lower], [p for p in points if p[1] < p_lower[1]])
    combo = list(combo1) + list(combo2)

    for p1, p2 in combo:
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])

        if any([x1 < p[0] < x2 and y1 < p[1] < y2 for p in points]):
            continue

        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        if area > ans:
            ans = area
            ans_rect = ((x1, y1), x2 - x1, y2 - y1)

    print(ans)

    # plot
    plt.figure(figsize=(10, 10))
    fig, ax = plt.subplots()
    sns.scatterplot(x=[p[0] for p in points], y=[p[1] for p in points], s=1)
    for p1, p2 in combinations(points, 2):
        if p1[0] == p2[0]:
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
        elif p1[1] == p2[1]:
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
    rect = patches.Rectangle(
        ans_rect[0],
        ans_rect[1],
        ans_rect[2],
        linewidth=1,
        edgecolor="#0f0f0f80",
        facecolor="none",
    )
    ax.add_patch(rect)

    plt.savefig("./2025/day9/plot.png")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main("input_demo.txt")
    main("input.txt")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f} seconds")
