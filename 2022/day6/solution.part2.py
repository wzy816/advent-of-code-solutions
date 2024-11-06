import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    from collections import Counter

    c = Counter()
    size = 14
    for i in range(len(data[0]) - 1):
        if i - size >= 0:
            k = data[0][i - size]
            if c[k] == 1:
                del c[k]
            else:
                c[k] -= 1
        c[data[0][i]] += 1
        if len(c.keys()) == size:
            print(i + 1)
            return
    # 3534


if __name__ == "__main__":
    main()
