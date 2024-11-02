import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    from itertools import combinations

    import numpy as np

    ans = 0
    low = 200000000000000
    high = 400000000000000
    for h1, h2 in combinations(data, 2):
        p1, v1 = h1.split(" @")
        p2, v2 = h2.split(" @")
        x1, y1, z1 = [int(i) for i in p1.split(",")]
        x2, y2, z2 = [int(i) for i in p2.split(", ")]
        vx1, vy1, vz1 = [int(i) for i in v1.split(", ")]
        vx2, vy2, vz2 = [int(i) for i in v2.split(", ")]

        A = np.array([[vx1, -vx2], [vy1, -vy2]])
        b = np.array([-x1 + x2, -y1 + y2])
        try:
            t = np.linalg.solve(A, b)
            if t[0] < 0 or t[1] < 0:
                continue
            x1 = x1 + vx1 * t[0]
            y1 = y1 + vy1 * t[0]
            x2 = x2 + vx2 * t[1]
            y2 = y2 + vy2 * t[1]

            if low <= x1 <= high and low <= y1 <= high:
                ans += 1
        except:
            pass
    print(ans)
    # 14046


if __name__ == "__main__":
    main()
