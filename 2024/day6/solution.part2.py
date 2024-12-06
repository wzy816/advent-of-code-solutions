import os

from tqdm import tqdm


def is_loop(map, start_i, start_j, start_direction):
    i = start_i
    j = start_j
    direction = start_direction
    rows = len(map)
    cols = len(map[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    # up=1,right=2,down=4,left=8
    while True:
        if visited[i][j] & direction > 0:
            return True

        visited[i][j] = visited[i][j] | direction

        if i == 0 and direction == 1:
            break
        elif i == rows - 1 and direction == 4:
            break
        elif j == 0 and direction == 8:
            break
        elif j == cols - 1 and direction == 2:
            break

        if direction == 1:
            if map[i - 1][j] == "#":
                direction = 2
            else:
                i -= 1
        elif direction == 4:
            if map[i + 1][j] == "#":
                direction = 8
            else:
                i += 1
        elif direction == 8:
            if map[i][j - 1] == "#":
                direction = 1
            else:
                j -= 1
        elif direction == 2:
            if map[i][j + 1] == "#":
                direction = 4
            else:
                j += 1

    return False


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    start_i = 0
    start_j = 0
    map = []
    candidates = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[0])):
            p = data[i][j]
            row.append(p)
            if p == "^":
                start_i = i
                start_j = j
            if p == ".":
                candidates.append((i, j))

        map.append(row)

    ans = 0
    for pos in tqdm(candidates):
        i, j = pos
        map[i][j] = "#"
        if is_loop(map, start_i, start_j, 1):
            ans += 1
        map[i][j] = "."

    print(ans)


if __name__ == "__main__":
    main()
