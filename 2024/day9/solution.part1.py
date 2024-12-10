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
    for i in range(0, len(disk_map), 2):
        files, free_space = disk_map[i], disk_map[i + 1]
        rep += [i // 2] * files
        rep += ["."] * free_space

    head = 0
    tail = len(rep) - 1
    while tail >= head:
        if rep[head] == "." and rep[tail] != ".":
            rep[head], rep[tail] = rep[tail], rep[head]

        if rep[tail] == ".":
            tail -= 1
        if rep[head] != ".":
            head += 1

    # cal checksum
    ans = 0
    for i in range(len(rep)):
        if rep[i] != ".":
            ans += i * rep[i]
    print(ans)


if __name__ == "__main__":
    main()
