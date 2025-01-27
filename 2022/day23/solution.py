import os
from collections import Counter, defaultdict


def propose(pos, grounds, ms):

    has_adj = False
    for d, deltas in ms:
        for delta in deltas:
            if pos + delta in grounds:
                has_adj = True
                break
    if not has_adj:
        return None

    for d, deltas in ms:
        has_adj = False
        for delta in deltas:
            if pos + delta in grounds:
                has_adj = True
        if not has_adj:
            return pos + deltas[0]


def display(grounds):
    min_x = min([g.real for g in grounds])
    max_x = max([g.real for g in grounds])
    min_y = min([g.imag for g in grounds])
    max_y = max([g.imag for g in grounds])

    for i in range(int(min_x), int(max_x) + 1):
        line = ""
        for j in range(int(min_y), int(max_y) + 1):
            if i + j * 1j in grounds:
                line += "#"
            else:
                line += "."
        print(line)
    print("\n")


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    grounds = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "#":
                grounds[i + 1j * j] = 1

    moves = [
        ("n", [-1, -1 - 1j, -1 + 1j]),
        ("s", [1, 1 - 1j, 1 + 1j]),
        ("w", [-1j, -1j - 1, -1j + 1]),
        ("e", [1j, 1j - 1, 1j + 1]),
    ]

    round = 0
    while True:
        ms = moves[round % 4 :] + moves[0 : round % 4]

        propose_grounds = defaultdict()

        for pos in grounds:
            next_pos = propose(pos, grounds, ms)
            if next_pos is None:
                next_pos = pos
            propose_grounds[next_pos] = propose_grounds.get(next_pos, []) + [pos]

        next_grounds = {}
        for k, v in propose_grounds.items():
            if len(v) == 1:
                # moved
                next_grounds[k] = 1
            else:
                # not move
                for pos in v:
                    next_grounds[pos] = 1

        # part1
        if round == 10:
            min_x = min([g.real for g in grounds])
            max_x = max([g.real for g in grounds])
            min_y = min([g.imag for g in grounds])
            max_y = max([g.imag for g in grounds])
            print((max_x - min_x + 1) * (max_y - min_y + 1) - len(grounds))

        # part2
        if set(next_grounds.keys()) == set(grounds.keys()):
            print(round + 1)
            break

        grounds = next_grounds.copy()
        round += 1


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
