import os
import re


def search_line(line):
    return len(re.findall(r"XMAS", line))


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    ans = 0

    # rows
    for i in range(rows):
        line = data[i]
        ans += search_line(line)
        ans += search_line(line[::-1])

    # cols
    for j in range(cols):
        line = "".join([data[i][j] for i in range(rows)])
        ans += search_line(line)
        ans += search_line(line[::-1])

    # diagonal
    for d in range(-rows, cols):
        line = "".join([data[i][i + d] for i in range(rows) if 0 <= i + d < cols])
        ans += search_line(line)
        ans += search_line(line[::-1])
        line = "".join(
            [
                data[i][cols - 1 - i - d]
                for i in range(rows)
                if 0 <= cols - 1 - i - d < cols
            ]
        )
        ans += search_line(line)
        ans += search_line(line[::-1])

    print(ans)


if __name__ == "__main__":
    main()
