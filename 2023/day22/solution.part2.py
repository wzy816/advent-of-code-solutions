def main():
    with open("./input.txt", "r") as f:
        data = f.read().split("\n")

    bricks = []
    for line in data:
        start, end = line.split("~")
        sx, sy, sz = map(int, start.split(","))
        ex, ey, ez = map(int, end.split(","))
        brick = (sx, sy, sz, ex, ey, ez)
        bricks.append(brick)

    def fall_once2(bs):
        occ = {}
        for b in bs:
            sx, sy, sz, ex, ey, ez = b
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    for z in range(sz, ez + 1):
                        occ[(x, y, z)] = 1

        new_bs = []
        fall_cnt = 0
        fall_idx = [0 for _ in range(len(bs))]
        for i, b in enumerate(bs):
            sx, sy, sz, ex, ey, ez = b
            if sz == 1:
                new_bs.append((sx, sy, sz, ex, ey, ez))
            else:
                has_support = False

                for x in range(sx, ex + 1):
                    for y in range(sy, ey + 1):
                        if (x, y, sz - 1) in occ:
                            has_support = True

                if has_support:
                    new_bs.append((sx, sy, sz, ex, ey, ez))
                else:
                    new_bs.append((sx, sy, sz - 1, ex, ey, ez - 1))
                    fall_cnt += 1
                    fall_idx[i] = 1

        return new_bs, fall_cnt, fall_idx

    # stablize
    while True:
        bricks, fall_cnt, fall_idx = fall_once2(bricks)
        if fall_cnt == 0:
            break

    ans = 0
    for i in range(len(bricks)):
        new_bricks = bricks[:i] + bricks[i + 1 :]

        new_fall_idx = [0 for _ in range(len(new_bricks))]
        while True:
            new_bricks, fall_cnt, fall_idx = fall_once2(new_bricks)
            if fall_cnt == 0:
                break
            new_fall_idx = [new_fall_idx[i] | fall_idx[i] for i in range(len(fall_idx))]
        ans += sum(new_fall_idx)

    print(ans)
    # 98167


if __name__ == "__main__":
    main()
