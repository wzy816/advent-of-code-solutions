import os


def is_safe(arr):
    n = len(arr)
    dif = [arr[i + 1] - arr[i] for i in range(n - 1)]
    asc = [d >= 1 and d <= 3 for d in dif]
    desc = [d >= -3 and d <= -1 for d in dif]
    return all(asc) or all(desc)


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:

        data = f.read().split("\n")

    safe = 0
    for line in data:
        line = [int(l) for l in line.split(" ")]
        if is_safe(line):
            safe += 1
        else:
            for i in range(len(line)):
                new_line = line[0:i] + line[i + 1 : len(line)]
                if is_safe(new_line):
                    safe += 1
                    break

    print(safe)


if __name__ == "__main__":
    main()
