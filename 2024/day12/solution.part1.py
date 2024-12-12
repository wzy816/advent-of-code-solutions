import os


def bfs(i, j, data, visited, id, region):

    visited[i][j] = 1

    if id not in region:
        region[id] = []
    region[id].append((i, j))

    label = data[i][j]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni > len(data) - 1 or nj < 0 or nj > len(data[0]) - 1:
            continue
        if visited[ni][nj] != 0:
            continue

        if data[ni][nj] == label:
            bfs(ni, nj, data, visited, id, region)


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])

    visited = [[0 for j in range(cols)] for i in range(rows)]
    region = {}  # id: [(i,j),(i2,j2),...]
    id = 1
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] != 0:
                continue
            bfs(i, j, data, visited, id, region)
            id += 1

    ans = 0
    for id, plots in region.items():
        area = len(plots)
        first_plot = plots[0]
        label = data[first_plot[0]][first_plot[1]]

        perimeter = 0
        for plot in plots:
            i, j = plot
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # adjacent plot
                ni, nj = i + di, j + dj
                if ni < 0 or ni > rows - 1 or nj < 0 or nj > cols - 1:
                    # side is on edge
                    perimeter += 1
                elif data[ni][nj] != label:
                    # adjacent plot has different label, this side is on perimeter
                    perimeter += 1
        ans += area * perimeter
    print(ans)


if __name__ == "__main__":
    main()
