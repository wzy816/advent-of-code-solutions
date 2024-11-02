import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    map = []
    for line in data:
        map.append(list(line))

    q = []
    q.append([0, 1, 0, {}])
    ans = 0

    while q:
        new_q = []

        for candidate in q:
            i, j, steps, visited = candidate

            if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
                continue
            elif (i, j) in visited:
                continue
            elif map[i][j] == "#":
                continue
            else:
                v2 = dict.copy(visited)
                v2[(i, j)] = 1

                if map[i][j] == ">":
                    new_q.append([i, j + 1, steps + 1, v2])
                elif map[i][j] == "<":
                    new_q.append([i, j - 1, steps + 1, v2])
                elif map[i][j] == "^":
                    new_q.append([i - 1, j, steps + 1, v2])
                elif map[i][j] == "v":
                    new_q.append([i + 1, j, steps + 1, v2])
                elif map[i][j] == ".":
                    # last row
                    if i == len(map) - 1:
                        ans = max(ans, steps)
                    else:
                        new_q.append([i + 1, j, steps + 1, v2])
                        new_q.append([i - 1, j, steps + 1, v2])
                        new_q.append([i, j + 1, steps + 1, v2])
                        new_q.append([i, j - 1, steps + 1, v2])
        q = new_q

    print(ans)
    # 2310


if __name__ == "__main__":
    main()
