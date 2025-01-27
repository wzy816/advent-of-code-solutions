import os
from collections import defaultdict


def trip(start, end, valley, wall, rows, cols):
    dirs = {">": 1j, "<": -1j, "^": -1, "v": 1}

    q = set([start])
    minutes = 0
    while q:
        next_valley = defaultdict(list)
        for pos, blizzards in valley.items():
            for blizzard in blizzards:
                new_pos = pos + dirs[blizzard]
                if new_pos.real == 0:
                    new_pos = complex(rows - 2, new_pos.imag)
                elif new_pos.real == rows - 1:
                    new_pos = complex(1, new_pos.imag)
                elif new_pos.imag == 0:
                    new_pos = complex(new_pos.real, cols - 2)
                elif new_pos.imag == cols - 1:
                    new_pos = complex(new_pos.real, 1)
                next_valley[new_pos].append(blizzard)

        new_q = set()
        for p in q:
            for dir in [1j, -1j, -1, 1, 0]:
                np = p + dir

                if (
                    np.real < 0
                    or np.real > rows - 1
                    or np.imag < 0
                    or np.imag > cols - 1
                ):
                    continue
                if np in next_valley:
                    continue
                if np in wall:
                    continue
                new_q.add(np)

        minutes += 1
        q = new_q.copy()
        valley = next_valley.copy()

        if end in q:
            return minutes, valley


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    rows, cols = len(data), len(data[0])

    valley = defaultdict(list)
    wall = defaultdict()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "#":
                wall[i + 1j * j] = 1
            elif char != ".":
                valley[i + 1j * j].append(char)

    start = 1j
    end = (rows - 1) + 1j * (cols - 2)

    # part1
    m1, v1 = trip(start, end, valley, wall, rows, cols)
    print(m1)

    # part2
    m2, v2 = trip(end, start, v1, wall, rows, cols)
    m3, v3 = trip(start, end, v2, wall, rows, cols)
    print(m2, m3)
    print(m1 + m2 + m3)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
