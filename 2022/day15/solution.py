import os
import re

from tqdm import tqdm


def no_beacon_range(s, b, y):
    manhattan_dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    y_diff = abs(s[1] - y)
    if y_diff > manhattan_dist:
        return []
    else:
        d = abs(manhattan_dist - y_diff)
        return [(s[0] - d, s[0] + d)]


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for r in ranges[1:]:
        if r[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
        else:
            merged.append(r)
    return merged


def no_beacon_ranges(sb, y):
    ranges = []
    for s, b in sb:
        ranges += no_beacon_range(s, b, y)

    return merge_ranges(ranges)


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    sb = []
    regex = r"Sensor at x=([+-]?\d+), y=([+-]?\d+): closest beacon is at x=([+-]?\d+), y=([+-]?\d+)"
    for line in data:
        sx, sy, bx, by = map(int, re.findall(regex, line)[0])
        sb.append(((sx, sy), (bx, by)))

    # part 1
    y = 2000000
    merged = no_beacon_ranges(sb, y)

    bxs_at_y = set([b[0] for _, b in sb if b[1] == y])
    ans = 0
    for m in merged:
        ans += m[1] - m[0] + 1
        for bx in bxs_at_y:
            if m[0] <= bx <= m[1]:
                ans -= 1
    print(ans)

    # part 2
    for distress_y in tqdm(range(0, 4000001)):
        merged = no_beacon_ranges(sb, distress_y)
        if any([m[0] <= 0 and m[1] >= 4000000 for m in merged]):
            continue

        print(merged)
        m2 = [m for m in merged if 0 <= m[0] <= 4000000 or 0 <= m[1] <= 4000000]
        m2.sort(key=lambda x: x[0])
        distress_x = m2[0][1] + 1
        print(4000000 * distress_x + distress_y)
        return


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
