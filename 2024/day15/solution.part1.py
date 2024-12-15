import os


def move_box(warehouse, p, direction):
    next_p = p + direction
    if warehouse[next_p] == "#":
        return

    if warehouse[next_p] == "O":
        move_box(warehouse, next_p, direction)

    if warehouse[next_p] == ".":
        warehouse[next_p] = "O"
        warehouse[p] = "."
    return


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read()

    h, m = data.split("\n\n")
    h = h.split("\n")

    warehouse = {}
    start = 0 + 0j
    for i in range(len(h)):
        for j in range(len(h[0])):
            warehouse[i + 1j * j] = h[i][j]
            if h[i][j] == "@":
                start = i + 1j * j

    directions = {"<": -1j, ">": 1j, "^": -1, "v": 1}

    moves = m.replace("\n", "")
    for move in moves:
        next_p = start + directions[move]

        if warehouse[next_p] == "O":
            move_box(warehouse, next_p, directions[move])

        if warehouse[next_p] == ".":
            warehouse[next_p] = "@"
            warehouse[start] = "."
            start = next_p

    ans = sum([100 * k.real + k.imag for k in warehouse if warehouse[k] == "O"])
    print(ans)


if __name__ == "__main__":
    main()
