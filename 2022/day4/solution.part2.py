import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    ans = 0
    for line in data:
        p1, p2 = line.split(",")
        s1, e1 = map(int, p1.split("-"))
        s2, e2 = map(int, p2.split("-"))

        if e1 < s2 or e2 < s1:
            continue
        ans += 1

    print(ans)
    # 891


if __name__ == "__main__":
    main()
