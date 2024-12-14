import os
import re


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    q = [[0, 0], [0, 0]]

    wide = 101
    tall = 103

    for line in data:
        p, v = line.split(" ")
        px, py = map(int, re.findall(r"p=(\d+),(\d+)", p)[0])
        vx, vy = map(int, re.findall(r"v=(-?\d+),(-?\d+)", v)[0])

        px2 = (px + vx * 100) % wide
        py2 = (py + vy * 100) % tall

        if px2 == wide // 2 or py2 == tall // 2:
            continue

        q[px2 < wide // 2][py2 < tall // 2] += 1

    print(q[0][0] * q[0][1] * q[1][0] * q[1][1])


if __name__ == "__main__":
    main()
