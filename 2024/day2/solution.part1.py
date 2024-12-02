import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:

        data = f.read().split("\n")

    safe = 0
    for line in data:
        line = [int(l) for l in line.split(" ")]

        n = len(line)
        dif = [line[i + 1] - line[i] for i in range(n - 1)]
        asc = [d >= 1 and d <= 3 for d in dif]
        desc = [d >= -3 and d <= -1 for d in dif]

        if all(asc) or all(desc):
            safe += 1
    print(safe)


if __name__ == "__main__":
    main()
