def main():
    with open("./input.txt", "r") as f:
        data = f.read().split("\n")

    grid = []
    locs = {}
    for ri, row in enumerate(data):
        r = []
        for ci, col in enumerate(row):
            r.append(col)
            if col == "S":
                locs[(ri, ci)] = 1
                r[ci] = "."
        grid.append(r)

    import numpy as np

    x = []
    y = []
    step = 0
    target = 26501365

    while step < target:

        step += 1
        new_locs = {}

        for k in locs:
            (i, j) = k
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                if (
                    grid[ni % len(grid)][nj % len(grid[0])] != "#"
                    and (ni, nj) not in new_locs
                ):
                    new_locs[(ni, nj)] = 1
        locs = new_locs

        # trick is
        # the answer fit in a polynomial regard some noise when step is small
        # so use values when step reaches the border
        # to fit the curve and pred
        if (step - 65) % 131 == 0:
            x.append(step)
            y.append(len(locs.keys()))
            if len(x) >= 3:
                z = np.polyfit(x=np.array(x), y=np.array(y), deg=2)
                p = np.poly1d(z)
                print("pred", step, p(target))

    print(step, y[-1])
    # 630661863455116

    # pred 327 630661863455116.4
    # pred 458 630661863455115.0
    # pred 589 630661863455116.2
    # pred 720 630661863455115.5
    # pred 851 630661863455115.0
    # pred 982 630661863455117.4
    # pred 1113 630661863455114.9
    # pred 1244 630661863455115.5
    # pred 1375 630661863455115.5
    # pred 1506 630661863455117.2


if __name__ == "__main__":
    main()
