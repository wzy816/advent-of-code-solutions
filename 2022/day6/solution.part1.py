import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    # string letter counter
    from collections import Counter

    c = Counter()
    for i in range(len(data[0]) - 1):
        if i - 4 >= 0:
            c[data[0][i - 4]] -= 1
            if c[data[0][i - 4]] == 0:
                del c[data[0][i - 4]]
        c[data[0][i]] += 1
        if len(c.keys()) == 4:
            print(i + 1, c)
            return
    # 1093


if __name__ == "__main__":
    main()
