import os


def plot(rocks, minx, maxx, miny, maxy):
    for y in range(int(miny), int(maxy) + 1):
        for x in range(int(minx), int(maxx) + 1):
            if x + 1j * y == 500 + 1j * int(miny):
                print("+", end="")
            if x + 1j * y in rocks:
                print(rocks[x + 1j * y], end="")
            else:
                print(".", end="")
        print("\n")


def loop(rocks, max_y, fall_through):
    ans = 0
    while True:
        loc = 500 + 0 * 1j

        # for part2
        # simulate falling sand until a unit of sand comes to rest at 500,0
        if loc in rocks:
            break

        while loc.imag < max_y:
            d = loc + 1j
            l = loc - 1 + 1j
            r = loc + 1 + 1j
            if d not in rocks:
                loc = d
            elif l not in rocks:
                loc = l
            elif r not in rocks:
                loc = r
            else:
                rocks[loc] = "o"
                break

        # rest on lines
        if loc.imag < max_y:
            ans += 1

        if loc.imag == max_y:
            if fall_through:
                # part 1, fall to endless void
                break
            else:
                # part 2, rest on floow
                rocks[loc] = "o"
                ans += 1
    return ans


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rocks = {}

    for line in data:
        points = line.split(" -> ")

        for i in range(len(points) - 1):
            x1, y1 = map(int, points[i].split(","))
            x2, y2 = map(int, points[i + 1].split(","))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    rocks[x + 1j * y] = "#"

    max_y = max([k.imag for k in rocks])

    # part 1
    print(loop(dict(rocks), max_y + 100, True))

    # part 2
    print(loop(dict(rocks), max_y + 2 - 1, False))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
