import os


def walk(map, visited, start_i, start_j, start_direction):
    i = start_i
    j = start_j
    direction = start_direction
    rows = len(map)
    cols = len(map[0])

    while True:
        visited[i][j] = 1

        if i == 0 and direction == "up":
            break
        elif i == rows - 1 and direction == "down":
            break
        elif j == 0 and direction == "left":
            break
        elif j == cols - 1 and direction == "right":
            break

        if direction == "up":
            if map[i - 1][j] == "#":
                direction = "right"
            else:
                i -= 1
        elif direction == "down":
            if map[i + 1][j] == "#":
                direction = "left"
            else:
                i += 1
        elif direction == "left":
            if map[i][j - 1] == "#":
                direction = "up"
            else:
                j -= 1
        elif direction == "right":
            if map[i][j + 1] == "#":
                direction = "down"
            else:
                j += 1


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    start_i = 0
    start_j = 0
    rows = len(data)
    cols = len(data[0])
    map = []
    visited = [[0 for _ in range(cols)] for j in range(cols)]
    for i in range(rows):
        row = []
        for j in range(cols):
            p = data[i][j]
            row.append(p)
            if p == "^":
                start_i = i
                start_j = j
        map.append(row)

    walk(map, visited, start_i, start_j, "up")

    print(sum([sum(row) for row in visited]))


if __name__ == "__main__":
    main()
