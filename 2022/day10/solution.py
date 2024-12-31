import os
from bisect import bisect_left


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    d = []
    x = 1
    c = 0

    for line in data:
        if line == "noop":
            c += 1
            d.append((c, x))
        elif line.startswith("addx"):
            _, v = line.split(" ")
            v = int(v)
            c += 1
            d.append((c, x))
            c += 1
            x += v
            d.append((c, x))

    # part1
    cycles = [20, 60, 100, 140, 180, 220]
    ans = 0
    for c in cycles:
        i = bisect_left(d, c - 1, key=lambda x: x[0])
        ans += d[i][1] * c
    print(ans)

    # part2
    screen = [["." for _ in range(40)] for _ in range(6)]
    for i in range(240):
        row = i // 40
        col = i % 40
        index = bisect_left(d, i, key=lambda x: x[0])
        x = d[index][1]
        if x - 1 <= col <= x + 1:
            screen[row][col] = "#"
    for row in screen:
        print("".join(row))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
