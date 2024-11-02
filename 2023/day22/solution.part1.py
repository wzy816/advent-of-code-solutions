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

    def fall_once(bs):
        occ = {}
        for b in bs:
            sx, sy, sz, ex, ey, ez = b
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    for z in range(sz, ez + 1):
                        occ[(x, y, z)] = 1

        new_bs = []
        fall_cnt = 0
        for b in bs:
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

        return new_bs, fall_cnt

    # stablize
    while True:
        bricks, fall_cnt = fall_once(bricks)
        if fall_cnt == 0:
            break

    ans = 0
    for i in range(len(bricks)):
        new_bricks = bricks[:i] + bricks[i + 1 :]
        _, fall_cnt = fall_once(new_bricks)
        if fall_cnt == 0:
            ans += 1
    print(ans)
    # 512


if __name__ == "__main__":
    main()
