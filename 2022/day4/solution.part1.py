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

        if (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2):
            ans += 1

    print(ans)
    # 625


if __name__ == "__main__":
    main()
