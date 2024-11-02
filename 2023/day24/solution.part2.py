import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    hs = []
    for h in data:
        p1, v1 = h.split(" @")
        x1, y1, z1 = [int(i) for i in p1.split(",")]
        vx1, vy1, vz1 = [int(i) for i in v1.split(", ")]
        hs.append((x1, y1, z1, vx1, vy1, vz1))

    import numpy as np

    def cal(i, hs):
        a = []
        b = []
        c = []
        d = []
        for h1, h2 in zip(hs[i : i + 4], hs[i + 1 : i + 5]):
            x1, y1, z1, vx1, vy1, vz1 = h1
            x2, y2, z2, vx2, vy2, vz2 = h2
            a.append([vy2 - vy1, vx1 - vx2, y1 - y2, x2 - x1])
            b.append([x2 * vy2 - y2 * vx2 - x1 * vy1 + y1 * vx1])
            c.append([vz2 - vz1, vx1 - vx2, z1 - z2, x2 - x1])
            d.append([x2 * vz2 - z2 * vx2 - x1 * vz1 + z1 * vx1])
        x, y, vx, vy = np.linalg.solve(np.array(a), np.array(b))
        _, z, _, vz = np.linalg.solve(np.array(c), np.array(d))
        return int(x[0] + y[0] + z[0])

    print(cal(0, hs))
    print(cal(6, hs))

    # 808107741406755
    # 808107741406756  (check)


if __name__ == "__main__":
    main()
