import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    rows = len(data)
    cols = len(data[0])
    ans = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if data[i][j] != "A":
                continue
            if (
                data[i - 1][j - 1] == "M"
                and data[i + 1][j - 1] == "M"
                and data[i + 1][j + 1] == "S"
                and data[i - 1][j + 1] == "S"
            ):
                ans += 1

            if (
                data[i - 1][j - 1] == "S"
                and data[i + 1][j - 1] == "M"
                and data[i + 1][j + 1] == "M"
                and data[i - 1][j + 1] == "S"
            ):
                ans += 1
            if (
                data[i - 1][j - 1] == "S"
                and data[i + 1][j - 1] == "S"
                and data[i + 1][j + 1] == "M"
                and data[i - 1][j + 1] == "M"
            ):
                ans += 1
            if (
                data[i - 1][j - 1] == "M"
                and data[i + 1][j - 1] == "S"
                and data[i + 1][j + 1] == "S"
                and data[i - 1][j + 1] == "M"
            ):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
