import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    p = []
    for line in data:
        half = int(len(line) / 2)
        first, second = line[:half], line[half:]
        p.append(list(set(first) & set(second))[0])

    ans = 0
    for i in p:
        if ord(i) <= ord("Z") and ord(i) >= ord("A"):
            ans += ord(i) - ord("A") + 27
        else:
            ans += ord(i) - ord("a") + 1

    print(ans)


if __name__ == "__main__":
    main()
