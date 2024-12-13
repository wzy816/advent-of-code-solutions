import os

import numpy as np


def is_int(num):
    return abs(num - round(num)) <= 1e-3


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read()

    tokens = 0

    for machine in data.split("\n\n"):
        btn_a, btn_b, prize = machine.split("\n")

        ax = int(btn_a.split("X+")[1].split(", ")[0])
        ay = int(btn_a.split("Y+")[1])
        bx = int(btn_b.split("X+")[1].split(", ")[0])
        by = int(btn_b.split("Y+")[1])
        px = int(prize.split("X=")[1].split(", ")[0])
        py = int(prize.split("Y=")[1])

        ma, mb = np.linalg.solve(np.array([[ax, bx], [ay, by]]), np.array([[px], [py]]))

        if is_int(ma[0]) and 0 <= ma[0] <= 100 and is_int(mb[0]) and 0 <= mb[0] <= 100:
            tokens += 3 * ma[0] + 1 * mb[0]

    print(tokens)


if __name__ == "__main__":
    main()
