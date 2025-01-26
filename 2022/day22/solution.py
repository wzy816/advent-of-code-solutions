import os
from functools import cache


def wrap_around(pos, direction, boards):
    while (pos - direction) in boards:
        pos -= direction
    return (pos, direction)


@cache
def cube_edge_mapping():
    # use an paper of input region shape to fold cube
    #
    #                     ^         ^
    #                     5         6
    #
    #                     r1        r2
    #                 ┌────────┐┌────────┐
    #                 │        ││        │
    #                 │        ││        │
    #                 │        ││        │
    #            <4 c1│        ││        │c3 2>
    #                 │        ││        │
    #                 │        ││        │
    #                 │        ││        │
    #                 └────────┘└────────┘
    #                 ┌────────┐    r5
    #                 │        │      1
    #                 │        │      v
    #                 │        │
    #            <3 c5│        │
    #                 │        │c6 <1
    #           3     │        │
    #           V     │        │
    #           r6    └────────┘
    #       ┌────────┐┌────────┐
    #       │        ││        │
    #       │        ││        │
    #       │        ││        │
    #  4> c8│        ││        │c10 <2
    #       │        ││        │
    #       │        ││        │
    #       │        ││        │
    #       └────────┘└────────┘
    #       ┌────────┐   r10
    #       │        │      7
    #       │        │      v
    #       │        │
    # 5> c12│        │c13 <7
    #       │        │
    #       │        │
    #       │        │
    #       └────────┘
    #           r12
    #
    #           ^
    #           6
    #
    def shift_up(row_edge):
        return [p - 1 for p in row_edge]

    def shift_left(col_edge):
        return [p - 1j for p in col_edge]

    dirs = {"v": 1, "^": -1, "<": -1j, ">": 1j}

    # r and c
    # note that some inner edges must be shifted to get right coordinates in pairs
    row_edges = []
    for r in range(5):
        for c in range(3):
            row_edges.append([r * 50 + (c * 50 + i) * 1j for i in range(50)])
    col_edges = []
    for r in range(4):
        for c in range(4):
            col_edges.append([r * 50 + i + c * 50 * 1j for i in range(50)])

    # 1 to 7
    pairs = [
        (shift_up(row_edges[5]), shift_left(col_edges[6]), "v", "<"),  # r5 1v -> c6 1<
        (shift_left(col_edges[3]), shift_left(reversed(col_edges[10])), ">", "<"),
        (col_edges[5], row_edges[6], "<", "v"),
        (col_edges[1], list(reversed(col_edges[8])), "<", ">"),
        (row_edges[1], col_edges[12], "^", ">"),
        (row_edges[2], shift_up(row_edges[12]), "^", "^"),
        (shift_up(row_edges[10]), shift_left(col_edges[13]), "v", "<"),
    ]

    mapping = {}
    for edge1, edge2, dir1, dir2 in pairs:
        for point1, point2 in zip(edge1, edge2):
            mapping[(point1, dirs[dir1])] = (point2, dirs[dir2])
            mapping[(point2, -dirs[dir2])] = (point1, -dirs[dir1])
    return mapping


def wrap_around_cube(pos, direction, boards):
    mapping = cube_edge_mapping()
    return mapping[(pos, direction)]


def walk(start_pos, start_direction, moves, boards, wrap_around_func):
    pos = start_pos
    direction = start_direction
    for move in moves:
        if move == "L":
            direction *= 1j
        elif move == "R":
            direction *= -1j
        else:
            move = int(move)
            for _ in range(int(move)):
                next_pos = pos + direction
                next_direction = direction

                if next_pos not in boards:
                    next_pos, next_direction = wrap_around_func(pos, direction, boards)

                if boards[next_pos] == ".":
                    pos = next_pos
                    direction = next_direction
                elif boards[next_pos] == "#":
                    break
    facing = {1j: 0, 1: 1, -1j: 2, -1: 3}
    return int(1000 * (pos.real + 1) + 4 * (pos.imag + 1) + facing[direction])


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n\n")

    boards = {}

    pos = None
    for i, line in enumerate(data[0].split("\n")):
        for j, char in enumerate(line):
            if char == " ":
                continue
            else:
                boards[i + 1j * j] = char

            if pos is None:
                pos = i + 1j * j
    moves = data[1].replace("L", " L ").replace("R", " R ").split(" ")

    # part1
    print(walk(pos, 1j, moves, boards, wrap_around))

    # part2
    print(walk(pos, 1j, moves, boards, wrap_around_cube))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
