import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    disk_map = list([int(num) for num in data[0]])
    if len(disk_map) % 2 != 0:
        disk_map.append(0)

    rep = []
    c = {}
    for i in range(0, len(disk_map), 2):
        files, free_space = disk_map[i], disk_map[i + 1]
        c[i // 2] = [files, files, free_space, len(rep)]

        rep += [i // 2] * files
        rep += ["."] * free_space
    # print(c)
    # print("".join([str(r) for r in rep]))

    for i in range(len(disk_map) // 2 - 1, -1, -1):

        # find first free j
        file_of_i, total_of_i, free_of_i, start_of_i = (
            c[i][0],
            c[i][1],
            c[i][2],
            c[i][3],
        )
        move_to_j = None
        for k, v in sorted(c.items(), key=lambda x: x[0]):
            # skip if not move to left
            if k == i:
                break

            # if k's free is enough to move i's files
            if v[2] >= file_of_i:
                move_to_j = k
                break

        if move_to_j is not None:
            # clear i to '.'
            for j in range(start_of_i, start_of_i + file_of_i):
                rep[j] = "."

            # fill j's '.' to i
            for j in range(file_of_i):
                rep[c[move_to_j][3] + c[move_to_j][1] + j] = i

            # update j's total
            c[move_to_j][1] = c[move_to_j][1] + file_of_i

            # update j's free
            c[move_to_j][2] = c[move_to_j][2] - file_of_i

            # update i's free to -1, set it not able to be moved to
            c[i][2] = -1  # move once

    # cal checksum
    ans = 0
    for i in range(len(rep)):
        if rep[i] != ".":
            ans += i * rep[i]
    print(ans)


if __name__ == "__main__":
    main()
