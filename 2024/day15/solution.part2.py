import os


def move_box_qigong(wh, p, di):

    next_p = p + di

    if di == 1j or di == -1j:
        if wh[next_p] == "#":
            return

        # move next one
        if wh[next_p] == "[" or wh[next_p] == "]":
            move_box_qigong(wh, next_p, di)

        # move current
        if wh[next_p] == ".":
            wh[next_p] = wh[p]
            wh[p] = "."

    if di == 1 or di == -1:

        if wh[next_p] == "#":
            return
        if wh[p] == "[" and wh[next_p + 1j] == "#":
            return
        if wh[p] == "]" and wh[next_p - 1j] == "#":
            return

        if wh[p] == "[":
            # move next one
            if wh[next_p] == "[":
                move_box_qigong(wh, next_p, di)
            if wh[next_p] == "]" and wh[next_p + 1j] == ".":
                move_box_qigong(wh, next_p, di)
            if wh[next_p] == "." and wh[next_p + 1j] == "[":
                move_box_qigong(wh, next_p + 1j, di)

            # move next two
            if wh[next_p] == "]" and wh[next_p + 1j] == "[":
                move_box_qigong(wh, next_p, di)
                move_box_qigong(wh, next_p + 1j, di)

            # move current
            if wh[next_p] == "." and wh[next_p + 1j] == ".":
                wh[next_p] = "["
                wh[next_p + 1j] = "]"
                wh[p] = "."
                wh[p + 1j] = "."

        if wh[p] == "]":
            # move next one
            if wh[next_p] == "]":
                move_box_qigong(wh, next_p, di)
            if wh[next_p] == "[" and wh[next_p - 1j] == ".":
                move_box_qigong(wh, next_p, di)
            if wh[next_p] == "." and wh[next_p - 1j] == "]":
                move_box_qigong(wh, next_p - 1j, di)

            # move next two
            if wh[next_p] == "[" and wh[next_p - 1j] == "]":
                move_box_qigong(wh, next_p, di)
                move_box_qigong(wh, next_p - 1j, di)

            # move current
            if wh[next_p] == "." and wh[next_p - 1j] == ".":
                wh[next_p] = "]"
                wh[next_p - 1j] = "["
                wh[p] = "."
                wh[p - 1j] = "."


# def display(wh, di):
#     rows = max([int(k.real) for k in wh]) + 1
#     cols = max([int(k.imag) for k in wh]) + 1
#     directions = {"<": -1j, ">": 1j, "^": -1, "v": 1}
#     move = [k for k, v in directions.items() if v == di][0]

#     for i in range(rows):
#         for j in range(cols):
#             if wh[i + 1j * j] == "@":
#                 print("\033[91m" + move + "\033[0m", end="")
#             else:
#                 print(wh[i + 1j * j], end="")
#         print("\n")


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read()

    warehouse = {}
    p = 0 + 0j

    h, m = data.split("\n\n")
    h = h.split("\n")

    # build [] from O
    for i in range(len(h)):
        for j in range(len(h[0])):
            if h[i][j] == "#":
                warehouse[i + 2j * j] = "#"
                warehouse[i + 2j * j + 1j] = "#"
            elif h[i][j] == "O":
                warehouse[i + 2j * j] = "["
                warehouse[i + 2j * j + 1j] = "]"
            elif h[i][j] == ".":
                warehouse[i + 2j * j] = h[i][j]
                warehouse[i + 2j * j + 1j] = h[i][j]
            elif h[i][j] == "@":
                warehouse[i + 2j * j] = "@"
                warehouse[i + 2j * j + 1j] = "."
                p = i + 2j * j

    directions = {"<": -1j, ">": 1j, "^": -1, "v": 1}

    moves = m.replace("\n", "")

    for move in moves:
        di = directions[move]
        next_p = p + di

        # solution:
        # in move_box_qigong()
        # every box is given a independent momentum to move
        # so case like this

        ####################
        ##................##
        ##....[]#.... ....##
        ##...[][].........##
        ##....[]..........##
        ##....^...........##
        ####################

        # will result in this

        ####################
        ##....[]..........##
        ##...[].#.... ....##
        ##.....[].........##
        ##....[]..........##
        ##....^...........##
        ####################

        # but in this game, all boxes either all move or all not move
        # so to compensate
        # if @ is not moved at last, reset warehouse to cached value

        w2 = warehouse.copy()
        p2 = p

        if warehouse[next_p] == "[" or warehouse[next_p] == "]":
            move_box_qigong(warehouse, next_p, di)

        if warehouse[next_p] == ".":
            warehouse[next_p] = "@"
            warehouse[p] = "."
            p = next_p

        if p == p2:
            warehouse = w2

    # display(warehouse, di)

    ans = sum([100 * k.real + k.imag for k in warehouse if warehouse[k] == "["])
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    # main("input_demo2.txt")
    # main("input_demo3.txt")
    main("input.txt")
