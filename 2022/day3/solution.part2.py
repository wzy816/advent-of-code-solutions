import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    p = []

    s = set()
    for i, line in enumerate(data):
        if i % 3 == 0:
            s = set(line)
        elif i % 3 == 1:
            s = s & set(line)
        elif i % 3 == 2:
            s = s & set(line)
            if i > 0:
                p.append(list(s)[0])

    ans = 0
    for i in p:
        if ord(i) <= ord("Z") and ord(i) >= ord("A"):
            ans += ord(i) - ord("A") + 27
        else:
            ans += ord(i) - ord("a") + 1

    print(ans)


if __name__ == "__main__":
    main()
