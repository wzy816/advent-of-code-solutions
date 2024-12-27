import os
from itertools import product


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n\n")

    locks = []
    keys = []

    for d in data:
        h = [0, 0, 0, 0, 0]
        for l in d.split("\n")[1:6]:
            for i, c in enumerate(l):
                if c == "#":
                    h[i] += 1
        if d[0:5] == "#####":
            locks.append(h)
        else:
            keys.append(h)

    ans = 0
    for k, l in product(keys, locks):
        if all([k[i] + l[i] <= 5 for i in range(5)]):
            ans += 1
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
