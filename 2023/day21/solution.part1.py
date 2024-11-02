from tqdm import tqdm


def main():
    with open("./input.txt", "r") as f:
        data = f.read().split("\n")

    grid = []
    si, sj = 0, 0
    for ri, row in enumerate(data):
        r = []
        for ci, col in enumerate(row):
            r.append(col)
            if col == "S":
                si = ri
                sj = ci
        grid.append(r)

    can = {f"{si}_{sj}": 1}
    for step in tqdm(range(64)):
        new_can = {}
        for k in can:
            i, j = map(int, k.split("_"))
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < len(grid)
                    and 0 <= nj < len(grid[0])
                    and grid[ni][nj] != "#"
                    and f"{ni}_{nj}" not in new_can
                ):
                    new_can[f"{ni}_{nj}"] = step
        can = dict.copy(new_can)
    print(len(can.keys()))
    # 3782

    # for i, row in enumerate(grid):
    #     for j, col in enumerate(row):
    #         if f"{i}_{j}" in can:
    #             print("O", end="")
    #         else:
    #             print(col, end="")
    #     print("")


if __name__ == "__main__":
    main()
